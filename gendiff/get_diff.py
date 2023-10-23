from copy import deepcopy

from gendiff.diff import make_diff
from gendiff.parsers.file_parser import parse_file


def update(f1: dict, f2: dict) -> dict:
    for k, v in f2.items():
        if not isinstance(f1, dict):
            f1 = f2
        elif isinstance(v, dict):
            r = update(f1.get(k, {}), v)
            f1[k] = r
        else:
            f1[k] = f2[k]
    return f1


def get_diff(path1: str, path2: str) -> list:
    f1_content, f2_content = parse_file(path1), parse_file(path2)
    overall = update(
        deepcopy(f1_content), deepcopy(f2_content)
    )

    diff = make_diff(overall, f1_content, f2_content)
    return diff
