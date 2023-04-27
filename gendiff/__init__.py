from gendiff.parsing import parse_files
from gendiff.diff import make_diff
from gendiff.stylish import out_stylish
from gendiff.plain import out_plain
from gendiff.json_output import out_json
from copy import deepcopy


def update(f1, f2):
    for k, v in f2.items():
        if not isinstance(f1, dict):
            f1 = f2
        elif isinstance(v, dict):
            r = update(f1.get(k, {}), v)
            f1[k] = r
        else:
            f1[k] = f2[k]
    return f1


def generate_diff(path1: str, path2: str, format_name: str = "stylish") -> str:
    """
    Generate the difference between two files.

    args:
    - path1 (str): the path to the first file to be compared.
    - path2 (str): the path to the second file to be compared.
    - format_name (str): the format to output the result in.
    Default is "stylish", options are "stylish", "plain", or "json".

    return:
    - str: the difference between the two files in the specified format.
    """
    f1, f2 = parse_files(path1, path2)
    overall = update(deepcopy(f1), deepcopy(f2))
    diff = make_diff(overall, f1, f2)
    match format_name:
        case "stylish":
            return out_stylish(diff)
        case "plain":
            return out_plain(diff)
        case "json":
            return out_json(diff)
        case _:
            return "Wrong format!\nPlease choose from stylish, plain or json"
