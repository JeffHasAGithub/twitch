import requests


def get(url: str, params: dict, **kwargs):
    response = requests.get(url, params, **kwargs)
    return response
