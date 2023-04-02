import yaml
import json


def parse_files(file_path1: str, file_path2: str) -> tuple:
    f1, f2 = {}, {}
    if file_path1.endswith('.json') and file_path2.endswith('.json'):
        with open(file_path1) as f1, open(file_path2) as f2:
            f1 = json.load(f1)
            f2 = json.load(f2)
    elif file_path1.endswith('.yaml') or file_path1.endswith('.yml'):
        if file_path2.endswith('.yaml') or file_path2.endswith('.yml'):
            with open(file_path1) as f1, open(file_path2) as f2:
                f1 = yaml.safe_load(open(file_path1))
                f2 = yaml.safe_load(open(file_path2))
    return f1, f2
