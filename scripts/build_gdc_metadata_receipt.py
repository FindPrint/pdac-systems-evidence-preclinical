#!/usr/bin/env python3
"""Construire un reçu de provenance à partir d'une réponse JSON GDC déjà obtenue.

Ce script ne contacte aucun service et ne lit aucune matrice RNA-seq. Il traite
uniquement les métadonnées retournées par l'API GDC des fichiers ouverts.
"""
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "external-links" / "gdc_open_rnaseq_metadata_response.json"
OUT_DIR = ROOT / "data" / "external-links"
TSV_OUT = OUT_DIR / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_MANIFEST.tsv"
JSON_OUT = OUT_DIR / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_RECEIPT.json"


def values(counter: Counter) -> dict[str, int]:
    return {str(k): int(v) for k, v in sorted(counter.items(), key=lambda item: str(item[0]))}


def main() -> None:
    raw = SOURCE.read_bytes()
    response = json.loads(raw)
    hits = response["data"]["hits"]

    rows: list[dict[str, str | int]] = []
    formats: Counter = Counter()
    workflows: Counter = Counter()
    sample_types: Counter = Counter()
    case_ids: set[str] = set()
    md5s: set[str] = set()

    for hit in hits:
        cases = hit.get("cases", [])
        case_ids.update(case.get("case_id", "") for case in cases if case.get("case_id"))
        samples = [sample for case in cases for sample in case.get("samples", [])]
        types = sorted({sample.get("sample_type", "") for sample in samples if sample.get("sample_type")})
        sample_type = ";".join(types) if types else ""
        sample_types[sample_type] += 1
        data_format = hit.get("data_format", "")
        workflow = hit.get("analysis", {}).get("workflow_type", "")
        formats[data_format] += 1
        workflows[workflow] += 1
        md5 = hit.get("md5sum", "")
        if md5:
            md5s.add(md5)
        rows.append(
            {
                "file_id": hit.get("file_id", hit.get("id", "")),
                "file_name": hit.get("file_name", ""),
                "md5sum": md5,
                "file_size_bytes": int(hit.get("file_size", 0)),
                "access": hit.get("access", ""),
                "data_type": hit.get("data_type", ""),
                "data_format": data_format,
                "experimental_strategy": hit.get("experimental_strategy", ""),
                "workflow_type": workflow,
                "case_ids": ";".join(sorted(case.get("case_id", "") for case in cases if case.get("case_id"))),
                "submitter_ids": ";".join(sorted(case.get("submitter_id", "") for case in cases if case.get("submitter_id"))),
                "sample_types": sample_type,
                "created_datetime": hit.get("created_datetime", ""),
                "updated_datetime": hit.get("updated_datetime", ""),
            }
        )

    rows.sort(key=lambda row: str(row["file_id"]))
    with TSV_OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    receipt = {
        "scope": "Metadonnees uniquement ; aucune quantification RNA-seq n'a ete telechargee ni analysee.",
        "source_file": str(SOURCE.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "api_pagination": response["data"].get("pagination", {}),
        "file_count": len(rows),
        "distinct_case_count": len(case_ids),
        "distinct_md5_count": len(md5s),
        "total_file_size_bytes": sum(int(row["file_size_bytes"]) for row in rows),
        "data_formats": values(formats),
        "workflow_types": values(workflows),
        "sample_types": values(sample_types),
        "manifest_file": str(TSV_OUT.relative_to(ROOT)),
        "manifest_sha256": hashlib.sha256(TSV_OUT.read_bytes()).hexdigest(),
        "query_date": "2026-08-26",
        "official_api": "https://api.gdc.cancer.gov/files",
        "project_id": "ORGANOID-PANCREATIC",
        "query_constraints": {
            "access": "open",
            "data_type": "Gene Expression Quantification",
            "experimental_strategy": "RNA-Seq",
        },
    }
    JSON_OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
