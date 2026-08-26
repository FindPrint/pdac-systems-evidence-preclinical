#!/usr/bin/env python3
"""Importer sous contrôle d'intégrité les quantifications RNA-seq ouvertes GDC.

Portée délibérément limitée au manifeste local ORGANOID-PANCREATIC déjà publié.
Ce programme ne lit ni ne transforme les valeurs contenues dans les TSV. Il télécharge
chaque fichier déclaré ouvert, calcule son MD5 et écrit un reçu de transfert.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "external-links" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_MANIFEST.tsv"
DESTINATION = ROOT / "data" / "raw" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_20260826"
RECEIPT = ROOT / "data" / "external-links" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_IMPORT_RECEIPT.json"
API_PREFIX = "https://api.gdc.cancer.gov/data/"
EXPECTED = {
    "access": "open",
    "data_type": "Gene Expression Quantification",
    "data_format": "TSV",
    "experimental_strategy": "RNA-Seq",
    "workflow_type": "STAR - Counts",
}
FILE_ID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
FILENAME_SUFFIX = ".rna_seq.augmented_star_gene_counts.tsv"
CHUNK_SIZE = 1024 * 1024
MAX_ATTEMPTS = 3


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_rows(rows: list[dict[str, str]]) -> None:
    if len(rows) != 55:
        raise ValueError(f"Le manifeste doit contenir exactement 55 lignes, pas {len(rows)}.")
    ids: set[str] = set()
    md5s: set[str] = set()
    for row in rows:
        for field, expected in EXPECTED.items():
            if row.get(field) != expected:
                raise ValueError(f"Contrainte invalide pour {row.get('file_id')}: {field}={row.get(field)!r}.")
        file_id = row.get("file_id", "")
        if not FILE_ID.fullmatch(file_id):
            raise ValueError(f"Identifiant GDC invalide: {file_id!r}.")
        if not row.get("file_name", "").endswith(FILENAME_SUFFIX):
            raise ValueError(f"Nom de fichier hors périmètre: {row.get('file_name')!r}.")
        md5 = row.get("md5sum", "")
        if not re.fullmatch(r"[0-9a-f]{32}", md5):
            raise ValueError(f"MD5 GDC absent ou invalide pour {file_id}.")
        if int(row.get("file_size_bytes", "0")) <= 0:
            raise ValueError(f"Taille GDC invalide pour {file_id}.")
        ids.add(file_id)
        md5s.add(md5)
    if len(ids) != 55 or len(md5s) != 55:
        raise ValueError("Les identifiants ou les MD5 du manifeste ne sont pas tous distincts.")


def md5_and_size(path: Path) -> tuple[str, int]:
    digest = hashlib.md5()
    size = 0
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(block)
            size += len(block)
    return digest.hexdigest(), size


def download_one(row: dict[str, str]) -> dict[str, object]:
    file_id = row["file_id"]
    expected_md5 = row["md5sum"]
    expected_size = int(row["file_size_bytes"])
    target = DESTINATION / row["file_name"]

    if target.exists():
        observed_md5, observed_size = md5_and_size(target)
        if observed_md5 == expected_md5 and observed_size == expected_size:
            return {
                "file_id": file_id,
                "file_name": target.name,
                "status": "already_verified",
                "expected_md5": expected_md5,
                "observed_md5": observed_md5,
                "expected_size_bytes": expected_size,
                "observed_size_bytes": observed_size,
                "local_sha256": sha256_file(target),
            }
        target.unlink()

    part = target.with_name(target.name + ".part")
    if part.exists():
        part.unlink()

    failure: str | None = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            request = urllib.request.Request(API_PREFIX + file_id, headers={"User-Agent": "pdac-systems-evidence-preclinical/1.0"})
            with urllib.request.urlopen(request, timeout=120) as response, part.open("wb") as output:
                digest = hashlib.md5()
                observed_size = 0
                for block in iter(lambda: response.read(CHUNK_SIZE), b""):
                    output.write(block)
                    digest.update(block)
                    observed_size += len(block)
            observed_md5 = digest.hexdigest()
            if observed_size != expected_size:
                raise ValueError(f"taille reçue {observed_size}, taille attendue {expected_size}")
            if observed_md5 != expected_md5:
                raise ValueError(f"MD5 reçu {observed_md5}, MD5 attendu {expected_md5}")
            part.replace(target)
            return {
                "file_id": file_id,
                "file_name": target.name,
                "status": "downloaded_and_verified",
                "expected_md5": expected_md5,
                "observed_md5": observed_md5,
                "expected_size_bytes": expected_size,
                "observed_size_bytes": observed_size,
                "local_sha256": sha256_file(target),
            }
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, OSError) as error:
            failure = f"tentative {attempt}/{MAX_ATTEMPTS}: {error}"
            part.unlink(missing_ok=True)
            if attempt < MAX_ATTEMPTS:
                time.sleep(attempt * 3)
    raise RuntimeError(f"Échec de téléchargement vérifié pour {file_id}: {failure}")


def main() -> None:
    manifest_sha256 = sha256_file(MANIFEST)
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    validate_rows(rows)
    DESTINATION.mkdir(parents=True, exist_ok=True)

    started_at = datetime.now(timezone.utc).isoformat()
    transfers = []
    try:
        for position, row in enumerate(rows, start=1):
            print(f"[{position}/{len(rows)}] {row['file_id']}", flush=True)
            transfers.append(download_one(row))
    except Exception:
        receipt = {
            "scope": "Import de quantifications RNA-seq ouvertes uniquement ; aucune analyse ni transformation du contenu TSV.",
            "status": "failed",
            "started_at_utc": started_at,
            "failed_after_verified_files": len(transfers),
            "manifest_file": str(MANIFEST.relative_to(ROOT)),
            "manifest_sha256": manifest_sha256,
            "destination": str(DESTINATION.relative_to(ROOT)),
            "transfers": transfers,
        }
        RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        raise

    status_counts = Counter(str(item["status"]) for item in transfers)
    receipt = {
        "scope": "Import de quantifications RNA-seq ouvertes uniquement ; aucune analyse ni transformation du contenu TSV.",
        "status": "complete",
        "started_at_utc": started_at,
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "project_id": "ORGANOID-PANCREATIC",
        "file_count": len(transfers),
        "total_expected_size_bytes": sum(int(item["expected_size_bytes"]) for item in transfers),
        "total_observed_size_bytes": sum(int(item["observed_size_bytes"]) for item in transfers),
        "all_md5_verified": all(item["expected_md5"] == item["observed_md5"] for item in transfers),
        "status_counts": dict(sorted(status_counts.items())),
        "manifest_file": str(MANIFEST.relative_to(ROOT)),
        "manifest_sha256": manifest_sha256,
        "destination": str(DESTINATION.relative_to(ROOT)),
        "transfers": transfers,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: receipt[key] for key in ("status", "file_count", "all_md5_verified", "total_observed_size_bytes")}, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERREUR: {exc}", file=sys.stderr)
        sys.exit(1)
