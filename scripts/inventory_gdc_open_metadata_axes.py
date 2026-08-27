#!/usr/bin/env python3
"""Inventorier les noms, types et couvertures des métadonnées GDC ouvertes.

Le script ne sérialise aucune valeur individuelle de métadonnée, aucune donnée
contrôlée et aucune valeur de quantification RNA-seq. Il recense seulement les
chemins de champs, leurs types JSON et leur présence dans les 55 fichiers.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "external-links" / "gdc_open_rnaseq_metadata_response.json"
RECEIPT = ROOT / "data" / "external-links" / "GDC_ORGANOID_PANCREATIC_OPEN_RNASEQ_METADATA_FIELD_INVENTORY.json"
EXPECTED_FILE_COUNT = 55
AXIS_TOKENS = ("time", "date", "day", "hour", "duration", "passage", "cycle", "dose", "concentration", "treatment", "treat", "condition", "stage", "spatial", "coordinate", "location", "serial", "sequence")


def json_type(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def collect_paths(value: object, prefix: str, paths: Counter[str], types: dict[str, Counter[str]]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else key
            paths[path] += 1
            types[path][json_type(child)] += 1
            collect_paths(child, path, paths, types)
    elif isinstance(value, list):
        for child in value:
            collect_paths(child, f"{prefix}[]", paths, types)


def main() -> None:
    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    hits = payload.get("data", {}).get("hits", [])
    if not isinstance(hits, list) or len(hits) != EXPECTED_FILE_COUNT:
        raise ValueError("La réponse GDC locale ne contient pas exactement 55 fichiers.")

    presence: Counter[str] = Counter()
    occurrences: Counter[str] = Counter()
    types: dict[str, Counter[str]] = defaultdict(Counter)
    for hit in hits:
        if not isinstance(hit, dict):
            raise ValueError("Structure de hit GDC inattendue.")
        file_paths: Counter[str] = Counter()
        file_types: dict[str, Counter[str]] = defaultdict(Counter)
        collect_paths(hit, "", file_paths, file_types)
        for path in file_paths:
            presence[path] += 1
            occurrences[path] += file_paths[path]
            types[path].update(file_types[path])

    fields = [
        {
            "path": path,
            "present_in_file_count": presence[path],
            "occurrence_count": occurrences[path],
            "json_types": dict(sorted(types[path].items())),
        }
        for path in sorted(presence)
    ]
    candidate_paths = [
        field["path"]
        for field in fields
        if any(token in field["path"].lower() for token in AXIS_TOKENS)
    ]
    receipt = {
        "scope": "Inventaire de noms, types JSON et couvertures des champs de la réponse GDC ouverte. Aucune valeur individuelle de métadonnée ni valeur RNA-seq n’est incluse.",
        "status": "complete",
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "project_id": "ORGANOID-PANCREATIC",
        "file_count": len(hits),
        "field_count": len(fields),
        "axis_keyword_candidates": candidate_paths,
        "fields": fields,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: receipt[key] for key in receipt if key != "fields"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
