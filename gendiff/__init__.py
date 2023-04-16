from gendiff.parsing import parse_files
from gendiff.diff import make_diff
from gendiff.stylish import out_stylish
from gendiff.plain import out_plain
from gendiff.json_output import out_json
from copy import deepcopy


def update(f1, f2):
    for k, v in f2.items():
        if isinstance(v, dict):
            f1[k] = update(f1.get(k, {}), v)
        else:
            f1[k] = v
    return f1


def generate_diff(path1: str, path2: str, format_name: str = "stylish") -> str:
    f1, f2 = parse_files(path1, path2)
    overall = update(deepcopy(f1), deepcopy(f2))
    diff = make_diff(overall, f1, f2)
    match format_name:
        case "stylish":
            return out_stylish(diff)
        case "plain":
            return out_plain(diff)
        case 'json':
            return out_json(diff)
        case _:
            return "Wrong format!\nPlease choose from stylish, plain or json"
