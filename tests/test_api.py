import unittest

from app import app


class ApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_predict_all(self) -> None:
        response = self.client.post("/predict", json={})
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["prediction"]["country"], "ALL")

    def test_predict_country(self) -> None:
        response = self.client.post("/predict", json={"country": "Spain"})
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["prediction"]["country"], "Spain")


if __name__ == "__main__":
    unittest.main()
