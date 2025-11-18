from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List

SAMPLE_DATA_PATH = Path(__file__).parent / "sample_data" / "invoices_sample.json"

# This loads invoices from a small JSON file.
# It's like a helper to make testing the API easier without manual copy-paste.
def load_invoices(data_path: Path = SAMPLE_DATA_PATH) -> List[Dict[str, object]]:
    with data_path.open("r", encoding="utf-8") as handler:
        return json.load(handler)

# This makes a simple summary of average revenue by country.
def summarize_by_country(records: Iterable[Dict[str, object]]) -> Dict[str, Dict[str, float]]:
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
