import requests
from typing import NamedTuple


class OAuth(NamedTuple):
    client_id: str
    client_secret: str
    access_token: str


def authenticate(client_id: str, client_secret: str) -> OAuth:
    url = "https://id.twitch.tv/oauth2/token"
    data = {"client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"}

    response = requests.get(url, data)
    oauth = OAuth(client_id, client_secret,
                  response.json()["access_token"])

    return oauth
