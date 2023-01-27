from typing import NamedTuple

from .http import post, extract_json


class OAuth(NamedTuple):
    """
    OAuth class holds immutable fields needed
    accessing Twitch API.
    """

    client_id: str
    client_secret: str
    access_token: str


def authenticate(client_id: str, client_secret: str) -> OAuth:
    """
    Authenticates with Twitch service and returns
    credentials in an instance of the OAuth class.
    """

    url = "https://id.twitch.tv/oauth2/token"
    data = {"client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"}

    json = extract_json(post(url, data))
    oauth = OAuth(client_id, client_secret,
                  json["access_token"])

    return oauth
