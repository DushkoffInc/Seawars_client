import json


class JSONObject:
    def __init__(self, dict):
        vars(self).update(dict)


def to_JSON(object):
    return json.dumps(object,
                      default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)
