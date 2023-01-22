import requests
import requests.exceptions

from .error import HttpError


def get(url: str, params: dict, **kwargs):
    response = requests.get(url, params, **kwargs)
    return response


def post(url: str, params: dict, **kwargs):
    response = requests.post(url, params, kwargs)
    return response
