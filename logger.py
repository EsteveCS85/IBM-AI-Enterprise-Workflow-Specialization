from __future__ import annotations

import csv
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


# This class handles logging predictions to a CSV file.
class PredictionLogger:
    # Initializes the logger with a directory for log files.
    def __init__(self, log_dir: Path = LOG_DIR):
        self.log_dir = log_dir

    # Determines the file path for today's log file.
    def _filepath(self) -> Path:
        today = datetime.utcnow().strftime("%Y-%m-%d")
        return self.log_dir / f"prediction-log-{today}.csv"

    # Logs prediction details to the CSV file.
    def log(self, *, country: str, runtime_ms: float, prediction: Dict[str, float], request_id: Optional[str] = None) -> Path:
        request_identifier = request_id or str(uuid.uuid4())
        path = self._filepath()
        file_exists = path.exists()
        with path.open("a", newline="", encoding="utf-8") as handler:
            writer = csv.DictWriter(
                handler,
                fieldnames=[
                    "request_id",
                    "timestamp",
                    "country",
                    "runtime_ms",
                    "average_revenue",
                    "model_version",
                ],
            )
            if not file_exists:
                writer.writeheader()
            writer.writerow(
                {
                    "request_id": request_identifier,
                    "timestamp": datetime.utcnow().isoformat(),
                    "country": country,
                    "runtime_ms": round(runtime_ms, 2),
                    "average_revenue": round(prediction.get("average_revenue", 0.0), 2),
                    "model_version": prediction.get("model_version", "unknown"),
                }
            )
        return path
