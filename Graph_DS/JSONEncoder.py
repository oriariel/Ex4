import json


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if "dict" in dir(o):
            return o.dict()
        return super().default(o)
