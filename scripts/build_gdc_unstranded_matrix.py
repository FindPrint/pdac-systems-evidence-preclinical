#!/usr/bin/env python3
"""Construire une matrice technique GDC `unstranded` sous contrôles gelés.

Ce script recopie textuellement la colonne `unstranded` après retrait des quatre
lignes techniques STAR. Il n'exécute aucune normalisation, statistique, filtrage,
comparaison biologique ni apprentissage de module.
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import sys
from contextlib import ExitStack
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTERNAL = ROOT / "data" / "external-links"
MANIFEST = EXTERNAL / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_MANIFEST.tsv"
IMPORT_RECEIPT = EXTERNAL / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_IMPORT_RECEIPT.json"
SCHEMA_RECEIPT = EXTERNAL / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_SCHEMA_RECEIPT.json"
QC_RECEIPT = EXTERNAL / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_NUMERIC_QC_RECEIPT.json"
RAW = ROOT / "data" / "raw" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_20260826"
OUT_DIR = ROOT / "data" / "processed" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_20260826"
MATRIX = OUT_DIR / "ORGANOID_PANCREATIC_unstranded_gene_by_file.tsv.gz"
FILE_MAP = OUT_DIR / "ORGANOID_PANCREATIC_file_map.tsv"
RECEIPT = EXTERNAL / "GDC_ORGANOID_PANCREATIC_UNSTRANDED_MATRIX_RECEIPT.json"
EXPECTED_MANIFEST_SHA256 = "f713edebf0f8afb20305b1472d480564e45ac31ce79e28350d7dde6ae496220b"
EXPECTED_HEADER = [
    "gene_id",
    "gene_name",
    "gene_type",
    "unstranded",
    "stranded_first",
    "stranded_second",
    "tpm_unstranded",
    "fpkm_unstranded",
    "fpkm_uq_unstranded",
]
TECHNICAL_SUMMARY_IDS = ("N_unmapped", "N_multimapping", "N_noFeature", "N_ambiguous")
EXPECTED_GENE_ROWS = 60660
EXPECTED_FILE_COUNT = 55
CHUNK_SIZE = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(block)
    return digest.hexdigest()


def md5_file(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_manifest() -> list[dict[str, str]]:
    if sha256_file(MANIFEST) != EXPECTED_MANIFEST_SHA256:
        raise ValueError("Le manifeste ne correspond pas à l’empreinte gelée du protocole.")
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if len(rows) != EXPECTED_FILE_COUNT:
        raise ValueError("Le manifeste ne contient pas 55 fichiers.")
    names = [row.get("file_name", "") for row in rows]
    ids = [row.get("file_id", "") for row in rows]
    if len(set(names)) != EXPECTED_FILE_COUNT or len(set(ids)) != EXPECTED_FILE_COUNT:
        raise ValueError("Noms ou file_id du manifeste absents ou non distincts.")
    return rows


def validate_previous_receipts() -> None:
    imported = load_json(IMPORT_RECEIPT)
    schema = load_json(SCHEMA_RECEIPT)
    qc = load_json(QC_RECEIPT)
    if not (imported.get("status") == "complete" and imported.get("all_md5_verified") is True and imported.get("file_count") == EXPECTED_FILE_COUNT):
        raise ValueError("Le reçu d’import ne valide pas les 55 fichiers.")
    if not (schema.get("status") == "complete" and schema.get("header_consistent") is True and schema.get("column_count_consistent") is True and schema.get("data_row_count_consistent") is True and schema.get("first_column_identifier_sequence_consistent") is True and schema.get("file_count") == EXPECTED_FILE_COUNT):
        raise ValueError("Le reçu de schéma ne valide pas la structure homogène.")
    status_counts = qc.get("file_status_counts", {})
    if not (qc.get("status") == "complete" and isinstance(status_counts, dict) and status_counts == {"pass": EXPECTED_FILE_COUNT} and qc.get("file_count") == EXPECTED_FILE_COUNT):
        raise ValueError("Le reçu de contrôle numérique ne valide pas les 55 fichiers.")


def verify_raw_md5(rows: list[dict[str, str]]) -> None:
    local_names = {path.name for path in RAW.glob("*.tsv")}
    manifest_names = {row["file_name"] for row in rows}
    if local_names != manifest_names:
        raise ValueError("L’ensemble de fichiers locaux ne correspond pas au manifeste.")
    for row in rows:
        path = RAW / row["file_name"]
        if md5_file(path) != row["md5sum"]:
            raise ValueError(f"MD5 divergent : {path.name}")


def open_reader(path: Path) -> tuple[object, csv.reader]:
    handle = path.open("r", encoding="utf-8", newline="")
    reader = csv.reader(handle, delimiter="\t")
    preamble = next(reader, None)
    header = next(reader, None)
    if preamble != ["# gene-model: GENCODE v36"] or header != EXPECTED_HEADER:
        handle.close()
        raise ValueError(f"Schéma divergent dans {path.name}.")
    return handle, reader


def build() -> dict[str, object]:
    rows = read_manifest()
    validate_previous_receipts()
    verify_raw_md5(rows)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    matrix_part = MATRIX.with_name(MATRIX.name + ".part")
    map_part = FILE_MAP.with_name(FILE_MAP.name + ".part")
    matrix_part.unlink(missing_ok=True)
    map_part.unlink(missing_ok=True)

    gene_order_digest = hashlib.sha256()
    technical_seen: set[str] = set()
    output_rows = 0

    try:
        with ExitStack() as stack:
            readers: list[csv.reader] = []
            for row in rows:
                handle, reader = open_reader(RAW / row["file_name"])
                stack.callback(handle.close)
                readers.append(reader)
            with gzip.open(matrix_part, "wt", encoding="utf-8", newline="") as matrix_handle:
                writer = csv.writer(matrix_handle, delimiter="\t", lineterminator="\n")
                writer.writerow(["gene_id", *[row["file_id"] for row in rows]])
                for line_index, grouped_rows in enumerate(zip(*readers), start=1):
                    first = grouped_rows[0]
                    if any(len(current) != len(EXPECTED_HEADER) for current in grouped_rows):
                        raise ValueError(f"Largeur tabulaire divergente à la ligne de données {line_index}.")
                    gene_id = first[0]
                    if any(current[0] != gene_id for current in grouped_rows[1:]):
                        raise ValueError(f"Ordre de gene_id divergent à la ligne de données {line_index}.")
                    if gene_id in TECHNICAL_SUMMARY_IDS:
                        technical_seen.add(gene_id)
                        continue
                    gene_order_digest.update(gene_id.encode("utf-8"))
                    gene_order_digest.update(b"\n")
                    writer.writerow([gene_id, *[current[3] for current in grouped_rows]])
                    output_rows += 1
                if any(next(reader, None) is not None for reader in readers):
                    raise ValueError("Longueurs de fichiers divergentes après lecture parallèle.")
        if technical_seen != set(TECHNICAL_SUMMARY_IDS):
            raise ValueError("Les quatre lignes techniques attendues ne sont pas toutes présentes.")
        if output_rows != EXPECTED_GENE_ROWS:
            raise ValueError(f"Nombre de gènes inattendu : {output_rows}.")
        with map_part.open("w", encoding="utf-8", newline="") as map_handle:
            writer = csv.DictWriter(map_handle, fieldnames=["file_id", "file_name", "case_ids"], delimiter="\t", lineterminator="\n")
            writer.writeheader()
            for row in rows:
                writer.writerow({key: row[key] for key in ("file_id", "file_name", "case_ids")})
        matrix_part.replace(MATRIX)
        map_part.replace(FILE_MAP)
    except Exception:
        matrix_part.unlink(missing_ok=True)
        map_part.unlink(missing_ok=True)
        raise

    return {
        "scope": "Construction technique locale de la matrice unstranded uniquement ; aucune normalisation, statistique, comparaison biologique ou activation de flux.",
        "status": "complete",
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "project_id": "ORGANOID-PANCREATIC",
        "source_manifest": str(MANIFEST.relative_to(ROOT)),
        "source_manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "input_file_count": len(rows),
        "output_gene_row_count": output_rows,
        "output_file_column_count": len(rows),
        "matrix_shape_gene_by_file": [output_rows, len(rows)],
        "technical_rows_excluded_per_file": list(TECHNICAL_SUMMARY_IDS),
        "gene_id_order_sha256": gene_order_digest.hexdigest(),
        "matrix_file": str(MATRIX.relative_to(ROOT)),
        "matrix_file_sha256": sha256_file(MATRIX),
        "file_map": str(FILE_MAP.relative_to(ROOT)),
        "file_map_sha256": sha256_file(FILE_MAP),
        "output_directory_git_ignored": True,
    }


def main() -> None:
    try:
        receipt = build()
        RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(receipt, indent=2, sort_keys=True))
    except Exception as exc:
        receipt = {
            "scope": "Construction technique locale de la matrice unstranded uniquement ; aucune normalisation, statistique, comparaison biologique ou activation de flux.",
            "status": "failed",
            "failed_at_utc": datetime.now(timezone.utc).isoformat(),
            "error": str(exc),
        }
        RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"ERREUR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
