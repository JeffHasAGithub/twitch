import requests
import requests.exceptions

from .error import HttpError


def get(url: str, params: dict, **kwargs):
    try:
        response = requests.get(url, params, **kwargs)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise HttpError(f"Http error: {e}")

    return response


def post(url: str, params: dict, **kwargs):
    try:
        response = requests.post(url, params, kwargs)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise HttpError(f"Http error: {e}")

    return response
