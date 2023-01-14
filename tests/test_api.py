import unittest
from unittest.mock import patch
from twitch.api.oauth import OAuth, authenticate


class TestOAuth(unittest.TestCase):
    def setUp(self):
        self.mock_get_patch = patch("twitch.api.oauth.requests.get")
        self.mock_get = self.mock_get_patch.start()

    def test_authenticate(self):
        self.mock_get.return_value.ok = True

        response = authenticate("aabbccdd", "eeffgghh")
        self.assertIsNotNone(response)

    def tearDown(self):
        self.mock_get_patch.stop()
