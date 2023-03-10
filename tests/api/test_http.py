import unittest
import requests
from unittest.mock import Mock, patch
from twitch.api.http import get, post, extract_json
from twitch.api.error import HttpError

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

        response = get("https://test.com/test")
        self.assertEqual(response.status_code, 200)

    @patch("twitch.api.http.requests.get")
    def test_get_bad_request(self, mock_get):
        mock_get.return_value = Mock(status_code=404)
        mock_get.side_effect = requests.exceptions.HTTPError(response=mock_get)

        with self.assertRaises(HttpError):
            get("https://test.com/test")

    @patch("twitch.api.http.requests.get")
    def test_get_bad_connection(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError()

        with self.assertRaises(HttpError):
            get("https://test.com/test")

    @patch("twitch.api.http.requests.post")
    def test_post_valid(self, mock_get):
        mock_get.return_value = Mock(status_code=200)

        response = post("https://test.com/test")
        self.assertEqual(response.status_code, 200)

    @patch("twitch.api.http.requests.post")
    def test_post_bad_request(self, mock_post):
        mock_post.return_value = Mock(status_code=404)
        mock_post.side_effect = requests.exceptions.HTTPError(response=mock_post)

        with self.assertRaises(HttpError):
            post("https://test.com/test")

    @patch("twitch.api.http.requests.post")
    def test_post_bad_connection(self, mock_post):
        mock_post.side_effect = requests.exceptions.ConnectionError()

        with self.assertRaises(HttpError):
            post("https://test.com/test")

    @patch("twitch.api.http.requests.get")
    def test_extract_json_valid(self, mock_get):
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = _json

        response = mock_get()
        json = extract_json(response)

        self.assertIsNotNone(json)
        self.assertDictEqual(json, _json)
