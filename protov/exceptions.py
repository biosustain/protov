from collections import deque
from typing import Tuple, Union


class ValidationError(Exception):
    def __init__(self, message: str, path: Tuple[Union[str, int], ...] = ()):
        self.message = message
        self.path = deque(path)

    def __str__(self):
        return "{} (at '{}')".format(self.message, '.'.join(map(str, self.path)))


class SchemaError(Exception):
    pass
