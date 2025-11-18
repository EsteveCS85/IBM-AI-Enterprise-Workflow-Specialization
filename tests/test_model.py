import unittest

from model import RevenueModel


class ModelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.model = RevenueModel()

    def test_predict_specific_country(self) -> None:
        result = self.model.predict(country="Spain")
        self.assertEqual(result["country"], "Spain")
        self.assertGreater(result["average_revenue"], 0)

    def test_predict_all_countries(self) -> None:
        result = self.model.predict()
        self.assertEqual(result["country"], "ALL")
        self.assertGreater(result["observations"], 0)


if __name__ == "__main__":
    unittest.main()
