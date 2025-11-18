import csv
import tempfile
import unittest
from pathlib import Path

from logger import PredictionLogger


class LoggerTests(unittest.TestCase):
    def test_log_creates_file_with_header(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            logger = PredictionLogger(log_dir=tmp_path)
            logger.log(
                country="Spain",
                runtime_ms=10.5,
                prediction={"average_revenue": 12000, "model_version": "0.1.0"},
                request_id="test",
            )
            files = list(tmp_path.glob("*.csv"))
            self.assertTrue(files)
            with files[0].open() as handler:
                reader = csv.DictReader(handler)
                rows = list(reader)
                self.assertEqual(rows[0]["country"], "Spain")


if __name__ == "__main__":
    unittest.main()
