from gendiff.parsing import parse_files
from gendiff.diff import make_diff
from gendiff.stylish import out_stylish
from copy import deepcopy


def update(f1, f2):
    for k, v in f2.items():
        if isinstance(v, dict):
            f1[k] = update(f1.get(k, {}), v)
        else:
            f1[k] = v
    return f1


def generate_diff(path1: str, path2: str, format: str = "stylish") -> str:
    f1, f2 = parse_files(path1, path2)
    overall = update(deepcopy(f1), deepcopy(f2))
    diff = make_diff(overall, f1, f2)
    match format:
        case "stylish":
            return out_stylish(diff)
        case _:
            return "Wrong format!"
