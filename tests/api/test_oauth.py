import unittest
from unittest.mock import Mock, patch
from twitch.api.oauth import authenticate


class TestOAuth(unittest.TestCase):
    def setUp(self):
        self.mock_post_patch = patch("twitch.api.oauth.post")
        self.mock_post = self.mock_post_patch.start()

        self.client_id = "aabbcc"
        self.client_secret = "ddeeff"
        self.access_token = "xxyyzz"

    def test_authenticate(self):
        self.mock_post.return_value = Mock(ok=True)
        self.mock_post.return_value.json.return_value = {"access_token":
                                                         self.access_token}

        oauth = authenticate(self.client_id, self.client_secret)

        self.assertIsNotNone(oauth)
        self.assertEqual(oauth.access_token, self.access_token)

    def tearDown(self):
        self.mock_post_patch.stop()
