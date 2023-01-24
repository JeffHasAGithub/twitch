import unittest
from unittest.mock import Mock, patch
from twitch.api.http import get, post, extract_json

_json = {"widget": {"debug": "on",
                    "window": {"title": "Sample Konfabulator Widget",
                               "name": "main_window",
                               "width": 500,
                               "height": 500},
                    "image": {"src": "Images/Sun.png",
                              "name": "sun1",
                              "hOffset": 250,
                              "vOffset": 250,
                              "alignment": "center"},
                    "text": {"data": "Click Here",
                             "size": 36,
                             "style": "bold",
                             "name": "text1",
                             "hOffset": 250,
                             "vOffset": 100,
                             "alignment": "center",
                             "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"}
                    }
         }


class TestHttp(unittest.TestCase):
    @patch("twitch.api.http.requests.get")
    def test_get_valid(self, mock_get):
        mock_get.return_value = Mock(status_code=200)

        response = get("https://test.com/test", {})
        self.assertEqual(response.status_code, 200)

    @patch("twitch.api.http.requests.post")
    def test_post_valid(self, mock_get):
        mock_get.return_value = Mock(status_code=200)

        response = post("https://test.com/test", {})
        self.assertEqual(response.status_code, 200)

    @patch("twitch.api.http.requests.get")
    def test_extract_json_valid(self, mock_get):
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = _json

        response = mock_get()
        json = extract_json(response)

        self.assertIsNotNone(json)
        self.assertDictEqual(json, _json)
