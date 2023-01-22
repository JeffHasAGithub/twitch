import unittest
from unittest.mock import Mock, patch
from twitch.api.http import get, post


class TestHttp(unittest.TestCase):
    @patch("twitch.api.http.requests.get")
    def test_get_valid(self, mock_get):
        mock_get.return_value = Mock(status_code=200)

        response = get("https://test.com/test", {})
        self.assertEqual(response.status_code, 200)
