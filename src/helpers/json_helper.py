from flask import request

class JsonHelper: # pylint: disable=too-few-public-methods
    @classmethod
    def get_value_from_request(cls, key, default = None):
        data = request.get_json()

        if key in data:
            return data[key]

        if default is not None:
            return default

        return None
