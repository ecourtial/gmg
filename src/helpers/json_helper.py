from typing import Any

from flask import request


class JsonHelper:  # pylint: disable=too-few-public-methods
    @classmethod
    def get_value_from_request(cls, key: str, default: Any = None) -> Any:
        data = request.get_json()

        if key in data:
            return data[key]

        if default is not None:
            return default

        return None
