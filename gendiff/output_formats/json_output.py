import json


def out_json(diff: list) -> str:
    return json.dumps(diff, indent=4, sort_keys=True)
