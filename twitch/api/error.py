class BaseError(Exception):
    def __init__(self, msg: str):
        self.msg = f"{__package__} {msg}"
