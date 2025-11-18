from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List

SAMPLE_DATA_PATH = Path(__file__).parent / "sample_data" / "invoices_sample.json"


def load_invoices(data_path: Path = SAMPLE_DATA_PATH) -> List[Dict[str, object]]:
    """Load invoices from a tiny JSON file.

    The helper mirrors the idea of automating ingestion so the API can be tested
    repeatably without manual copy/paste steps.
    """

    with data_path.open("r", encoding="utf-8") as handler:
        return json.load(handler)


def summarize_by_country(records: Iterable[Dict[str, object]]) -> Dict[str, Dict[str, float]]:
    """Generate average revenue per country in a very small way."""

    totals: Dict[str, float] = {}
    counts: Dict[str, int] = {}
    for row in records:
        country = str(row.get("country", "Unknown"))
        revenue = float(row.get("revenue", 0.0))
        totals[country] = totals.get(country, 0.0) + revenue
        counts[country] = counts.get(country, 0) + 1

    summary: Dict[str, Dict[str, float]] = {}
    for country, total in totals.items():
        summary[country] = {
            "average_revenue": total / max(counts[country], 1),
            "observations": counts[country],
        }
    return summary
