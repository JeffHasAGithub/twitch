import requests
import requests.exceptions

from .error import HttpError, JsonError


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


def extract_json(response: requests.Response, **kwargs):
    if not response:
        return None

    try:
        json = response.json(**kwargs)
    except requests.exceptions.InvalidJSONError:
        raise JsonError("Json error: invalid JSON")

    return json
