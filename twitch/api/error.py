class ApiError(Exception):
    """Base API Error"""


class HttpError(ApiError):
    """Http Error"""


class JsonError(ApiError):
    """Json Error"""
