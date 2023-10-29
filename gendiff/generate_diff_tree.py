from copy import deepcopy

from gendiff.parser import parse_data
from gendiff.diff_tree import make_diff
from gendiff.output_formats import generate_output


def update(dict1: dict, dict2: dict) -> dict:
    """recursively update a dictionary with another dictionary"""
    for k, v in dict2.items():
        if not isinstance(dict1, dict):
            dict1 = dict2
        elif isinstance(v, dict):
            r = update(dict1.get(k, {}), v)
            dict1[k] = r
        else:
            dict1[k] = dict2[k]
    return dict1


def generate_diff(path1: str, path2: str, format_name: str = 'stylish') -> str:
    f1_content, f2_content = parse_data(path1), parse_data(path2)
    overall = update(deepcopy(f1_content), deepcopy(f2_content))

    diff = make_diff(overall, f1_content, f2_content)
    return generate_output(diff, format_name)
