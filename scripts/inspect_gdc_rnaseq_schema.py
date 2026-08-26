#!/usr/bin/env python3
"""Inspecter la structure de TSV GDC sans analyser les quantifications.

Cette inspection est restreinte aux en-têtes, au nombre de colonnes et de lignes,
à l'identifiant de la première colonne (présence et empreinte) et à la cohérence
inter-fichiers. Les valeurs de quantification ne sont ni stockées, ni converties,
ni résumées, ni comparées.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "external-links" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_MANIFEST.tsv"
RAW = ROOT / "data" / "raw" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_20260826"
RECEIPT = ROOT / "data" / "external-links" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_SCHEMA_RECEIPT.json"
EXPECTED_FILE_COUNT = 55


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def read_manifest() -> list[dict[str, str]]:
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if len(rows) != EXPECTED_FILE_COUNT:
        raise ValueError(f"Le manifeste doit contenir {EXPECTED_FILE_COUNT} fichiers, pas {len(rows)}.")
    names = [row.get("file_name", "") for row in rows]
    if len(set(names)) != EXPECTED_FILE_COUNT or any(not name for name in names):
        raise ValueError("Noms de fichier manifestes absents ou non distincts.")
    return rows


def inspect_one(path: Path) -> dict[str, object]:
    first_column_ids = hashlib.sha256()
    row_count = 0
    expected_width: int | None = None
    header: list[str] | None = None
    preamble: list[str] = []

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        for line_number, row in enumerate(reader, start=1):
            if header is None:
                if len(row) == 1 and row[0].startswith("#"):
                    preamble.append(row[0])
                    continue
                if not row or any(column == "" for column in row):
                    raise ValueError(f"En-tête vide ou colonne sans nom dans {path.name}.")
                if len(set(row)) != len(row):
                    raise ValueError(f"Colonnes dupliquées dans {path.name}.")
                header = row
                expected_width = len(row)
                continue
            if expected_width is None or len(row) != expected_width:
                raise ValueError(f"Largeur tabulaire divergente dans {path.name}, ligne {line_number}.")
            if not row[0]:
                raise ValueError(f"Identifiant primaire vide dans {path.name}, ligne {line_number}.")
            # Seul l'identifiant de la première colonne est haché. Aucune autre
            # colonne, en particulier aucune valeur de quantification, n'est lue.
            first_column_ids.update(row[0].encode("utf-8"))
            first_column_ids.update(b"\n")
            row_count += 1

    if header is None or expected_width is None:
        raise ValueError(f"Fichier vide: {path.name}.")
    return {
        "file_name": path.name,
        "column_count": expected_width,
        "data_row_count": row_count,
        "header": header,
        "header_sha256": sha256_bytes("\t".join(header).encode("utf-8")),
        "preamble": preamble,
        "preamble_line_count": len(preamble),
        "first_column_name": header[0],
        "first_column_identifier_sequence_sha256": first_column_ids.hexdigest(),
    }


def main() -> None:
    manifest_rows = read_manifest()
    expected_names = {row["file_name"] for row in manifest_rows}
    local_paths = {path.name: path for path in RAW.glob("*.tsv")}
    if set(local_paths) != expected_names:
        missing = sorted(expected_names - set(local_paths))
        unexpected = sorted(set(local_paths) - expected_names)
        raise ValueError(f"Écart manifeste/local ; manquants={missing}, inattendus={unexpected}.")

    inspected = [inspect_one(local_paths[row["file_name"]]) for row in manifest_rows]
    headers = Counter(item["header_sha256"] for item in inspected)
    widths = Counter(item["column_count"] for item in inspected)
    rows = Counter(item["data_row_count"] for item in inspected)
    identifier_sequences = Counter(item["first_column_identifier_sequence_sha256"] for item in inspected)

    receipt = {
        "scope": "Inspection de schéma uniquement : en-têtes, largeur tabulaire, nombre de lignes et empreintes de la première colonne. Aucune valeur de quantification n'a été stockée, convertie, résumée ou comparée.",
        "status": "complete",
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "project_id": "ORGANOID-PANCREATIC",
        "manifest_file": str(MANIFEST.relative_to(ROOT)),
        "raw_directory": str(RAW.relative_to(ROOT)),
        "file_count": len(inspected),
        "distinct_header_count": len(headers),
        "distinct_column_count": len(widths),
        "distinct_data_row_count": len(rows),
        "distinct_first_column_identifier_sequence_count": len(identifier_sequences),
        "header_consistent": len(headers) == 1,
        "column_count_consistent": len(widths) == 1,
        "data_row_count_consistent": len(rows) == 1,
        "first_column_identifier_sequence_consistent": len(identifier_sequences) == 1,
        "schema": inspected,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: receipt[key] for key in receipt if key != "schema"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERREUR: {exc}", file=sys.stderr)
        sys.exit(1)
