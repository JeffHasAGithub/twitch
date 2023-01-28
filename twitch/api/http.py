import requests
import requests.exceptions

from .error import HttpError, JsonError


def get(url: str, **kwargs):
    """
    Perform GET request and return response.
    Raise HttpError on bad request.
    """

    try:
        response = requests.get(url, **kwargs)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise HttpError(f"Http error: {e.response.status_code}")
    except requests.exceptions.ConnectionError:
        raise HttpError("Http error: could not connect")

    return response


def post(url: str, **kwargs):
    """
    Perform POST request and return response.
    Raise HttpError on bad request.
    """

    try:
        response = requests.post(url, **kwargs)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise HttpError(f"Http error: {e.response.status_code}")
    except requests.exceptions.ConnectionError:
        raise HttpError("Http error: could not connect")

    return response


def extract_json(response: requests.Response, **kwargs):
    """
    Extract JSON from given instance of requests.Response class.
    Raise JsonError on invalid JSON.

    Return dict if JSON is valid, None otherwise.
    """
    if not response:
        return None

    try:
        json = response.json(**kwargs)
    except requests.exceptions.InvalidJSONError:
        raise JsonError("Json error: invalid JSON")

    return json
