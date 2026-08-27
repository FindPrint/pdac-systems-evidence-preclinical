#!/usr/bin/env python3
"""Contrôle qualité numérique limité des TSV GDC RNA-seq.

Le script vérifie les formats, domaines et identifiants. Il ne calcule aucune
statistique d'expression et ne sauvegarde aucune valeur individuelle.
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "external-links" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_MANIFEST.tsv"
RAW = ROOT / "data" / "raw" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_20260826"
RECEIPT = ROOT / "data" / "external-links" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_NUMERIC_QC_RECEIPT.json"
EXPECTED_FILE_COUNT = 55
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
INTEGER_COLUMNS = {"unstranded", "stranded_first", "stranded_second"}
DECIMAL_COLUMNS = {"tpm_unstranded", "fpkm_unstranded", "fpkm_uq_unstranded"}
QUANT_COLUMNS = INTEGER_COLUMNS | DECIMAL_COLUMNS
TECHNICAL_SUMMARY_IDS = {"N_unmapped", "N_multimapping", "N_noFeature", "N_ambiguous"}


def read_manifest() -> list[str]:
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    names = [row.get("file_name", "") for row in rows]
    if len(names) != EXPECTED_FILE_COUNT or len(set(names)) != EXPECTED_FILE_COUNT or any(not item for item in names):
        raise ValueError("Le manifeste local ne contient pas exactement 55 noms de fichiers distincts.")
    return names


def fresh_counts() -> dict[str, int]:
    return {"empty": 0, "non_numeric": 0, "non_finite": 0, "negative": 0, "non_integer": 0}


def validate_numeric(raw: str, integer_required: bool, counts: dict[str, int]) -> None:
    if raw == "":
        counts["empty"] += 1
        return
    try:
        value = Decimal(raw)
    except InvalidOperation:
        counts["non_numeric"] += 1
        return
    if not value.is_finite():
        counts["non_finite"] += 1
        return
    if value < 0:
        counts["negative"] += 1
    if integer_required and value != value.to_integral_value():
        counts["non_integer"] += 1


def inspect_one(path: Path) -> dict[str, object]:
    gene_ids: set[str] = set()
    duplicate_gene_ids = 0
    data_rows = 0
    missing_gene_id = 0
    missing_gene_name = 0
    missing_gene_type = 0
    technical_summary_ids_seen: set[str] = set()
    technical_summary_rows = 0
    issues = {column: fresh_counts() for column in EXPECTED_HEADER[3:]}

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        preamble = next(reader, None)
        header = next(reader, None)
        if preamble != ["# gene-model: GENCODE v36"]:
            raise ValueError(f"Préambule inattendu dans {path.name}.")
        if header != EXPECTED_HEADER:
            raise ValueError(f"En-tête inattendu dans {path.name}.")
        for line_number, row in enumerate(reader, start=3):
            if len(row) != len(EXPECTED_HEADER):
                raise ValueError(f"Largeur tabulaire divergente dans {path.name}, ligne {line_number}.")
            data_rows += 1
            gene_id, gene_name, gene_type = row[:3]
            if gene_id == "":
                missing_gene_id += 1
            elif gene_id in gene_ids:
                duplicate_gene_ids += 1
            else:
                gene_ids.add(gene_id)
            if gene_id in TECHNICAL_SUMMARY_IDS:
                technical_summary_ids_seen.add(gene_id)
                technical_summary_rows += 1
                # Les lignes techniques restent soumises aux contrôles des trois
                # colonnes de compte. Les annotations de gène et transformations
                # absentes ne sont pas assimilées à des anomalies de gène.
                for column, raw in zip(EXPECTED_HEADER[3:6], row[3:6]):
                    validate_numeric(raw, True, issues[column])
                continue
            if gene_name == "":
                missing_gene_name += 1
            if gene_type == "":
                missing_gene_type += 1
            for column, raw in zip(EXPECTED_HEADER[3:], row[3:]):
                validate_numeric(raw, column in INTEGER_COLUMNS, issues[column])

    technical_summary_id_missing_count = len(TECHNICAL_SUMMARY_IDS - technical_summary_ids_seen)
    technical_summary_id_duplicate_count = technical_summary_rows - len(technical_summary_ids_seen)
    anomaly_count = missing_gene_id + duplicate_gene_ids + missing_gene_name + missing_gene_type
    anomaly_count += technical_summary_id_missing_count + technical_summary_id_duplicate_count
    anomaly_count += sum(sum(column_counts.values()) for column_counts in issues.values())
    return {
        "file_name": path.name,
        "data_row_count": data_rows,
        "gene_id_missing_count": missing_gene_id,
        "gene_id_duplicate_count": duplicate_gene_ids,
        "gene_name_missing_count": missing_gene_name,
        "gene_type_missing_count": missing_gene_type,
        "technical_summary_row_count": technical_summary_rows,
        "technical_summary_id_missing_count": technical_summary_id_missing_count,
        "technical_summary_id_duplicate_count": technical_summary_id_duplicate_count,
        "numeric_issue_counts": issues,
        "anomaly_count": anomaly_count,
        "status": "pass" if anomaly_count == 0 else "flagged",
    }


def add_counts(total: dict[str, dict[str, int]], current: dict[str, dict[str, int]]) -> None:
    for column, counters in current.items():
        for label, count in counters.items():
            total[column][label] += count


def main() -> None:
    expected_names = set(read_manifest())
    local_paths = {path.name: path for path in RAW.glob("*.tsv")}
    if set(local_paths) != expected_names:
        raise ValueError("Les fichiers locaux ne correspondent plus exactement au manifeste.")

    records = [inspect_one(local_paths[name]) for name in sorted(expected_names)]
    aggregate_issues = {column: fresh_counts() for column in EXPECTED_HEADER[3:]}
    for record in records:
        add_counts(aggregate_issues, record["numeric_issue_counts"])

    status_counts = Counter(str(record["status"]) for record in records)
    identifier_issues = {
        "gene_id_missing_count": sum(int(record["gene_id_missing_count"]) for record in records),
        "gene_id_duplicate_count": sum(int(record["gene_id_duplicate_count"]) for record in records),
        "gene_name_missing_count": sum(int(record["gene_name_missing_count"]) for record in records),
        "gene_type_missing_count": sum(int(record["gene_type_missing_count"]) for record in records),
        "technical_summary_row_count": sum(int(record["technical_summary_row_count"]) for record in records),
        "technical_summary_id_missing_count": sum(int(record["technical_summary_id_missing_count"]) for record in records),
        "technical_summary_id_duplicate_count": sum(int(record["technical_summary_id_duplicate_count"]) for record in records),
    }
    receipt = {
        "scope": "Contrôle qualité numérique limité : validité syntaxique, finitude, non-négativité, intégralité des champs et unicité des gene_id. Aucune valeur individuelle, statistique d'expression, normalisation ou comparaison biologique n'est incluse.",
        "status": "complete",
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "project_id": "ORGANOID-PANCREATIC",
        "file_count": len(records),
        "expected_header": EXPECTED_HEADER,
        "file_status_counts": dict(sorted(status_counts.items())),
        "identifier_issue_counts": identifier_issues,
        "numeric_issue_counts": aggregate_issues,
        "files": records,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: receipt[key] for key in receipt if key != "files"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERREUR: {exc}", file=sys.stderr)
        sys.exit(1)
