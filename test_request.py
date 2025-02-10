import os.path
import unittest
from unittest.mock import patch
from request import retrieve_photo, retrieve_quote

class TestRequest(unittest.TestCase):
    @patch('request.requests.get')
    def test_retrieve_quote(self, mock_get):
        mock_get.return_value.status = 200
        mock_get.return_value.json.return_value = [{"quote": "Generic Coffee Quote."}]

        result = retrieve_quote()
        self.assertEqual(result, "Generic Coffee Quote.")

if __name__ == "__main__":
    unittest.main()