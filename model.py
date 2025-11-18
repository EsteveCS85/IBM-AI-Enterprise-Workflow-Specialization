from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, Optional

from data_ingestion import summarize_by_country

MODEL_PATH = Path(__file__).parent / "models" / "model_state.json"


class RevenueModel:
    """Loads pre-computed averages and returns basic predictions."""

    def __init__(self, serialized_path: Path = MODEL_PATH):
        self.serialized_path = serialized_path
        self.model_version = ""
        self.model_version_note = ""
        self.country_stats: Dict[str, Dict[str, float]] = {}
        self.all_stats: Dict[str, float] = {}
        self._load()

    def _load(self) -> None:
        with self.serialized_path.open("r", encoding="utf-8") as handler:
            payload = json.load(handler)
        self.model_version = payload.get("model_version", "unknown")
        self.model_version_note = payload.get("model_version_note", "")
        self.country_stats = payload.get("country_stats", {})
        self.all_stats = payload.get("all_countries", {})

    def predict(self, country: Optional[str] = None) -> Dict[str, float]:
        """Return a simple average revenue prediction."""

        if country:
            stats = self.country_stats.get(country)
            if not stats:
                return {
                    "country": country,
                    "average_revenue": 0.0,
                    "observations": 0,
                    "model_version": self.model_version,
                }
            return {
                "country": country,
                "average_revenue": stats.get("average_revenue", 0.0),
                "observations": stats.get("observations", 0),
                "model_version": self.model_version,
            }

        return {
            "country": "ALL",
            "average_revenue": self.all_stats.get("average_revenue", 0.0),
            "observations": self.all_stats.get("observations", 0),
            "model_version": self.model_version,
        }


def train_from_records(records: Iterable[Dict[str, object]], target_path: Path = MODEL_PATH) -> Dict[str, object]:
    """Re-compute averages and save them to the serialized JSON file."""

    summary = summarize_by_country(records)
    total_revenue = 0.0
    total_obs = 0
    for stats in summary.values():
        total_revenue += stats["average_revenue"] * stats["observations"]
        total_obs += stats["observations"]

    payload = {
        "model_version": "0.1.0",
        "model_version_note": "Average revenue per country using sample invoices",
        "country_stats": summary,
        "all_countries": {
            "average_revenue": total_revenue / max(total_obs, 1),
            "observations": total_obs,
        },
    }

    with target_path.open("w", encoding="utf-8") as handler:
        json.dump(payload, handler, indent=2)

    return payload
