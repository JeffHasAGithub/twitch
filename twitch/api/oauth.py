import requests
from typing import NamedTuple


class OAuth(NamedTuple):
    client_id: str
    client_secret: str
    access_token: str
