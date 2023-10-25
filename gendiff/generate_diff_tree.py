from copy import deepcopy

from gendiff.file_parser import parse_file
from gendiff.diff_tree import make_diff

from gendiff.output_formats.json_output import out_json
from gendiff.output_formats.plain import out_plain
from gendiff.output_formats.stylish import out_stylish


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


def generate_diff(path1: str, path2: str, format_name: str = 'stylish') -> str:
    f1_content, f2_content = parse_file(path1), parse_file(path2)
    overall = update(deepcopy(f1_content), deepcopy(f2_content))

    diff = make_diff(overall, f1_content, f2_content)
    match format_name:
        case 'stylish':
            return out_stylish(diff)
        case 'plain':
            return out_plain(diff)
        case 'json':
            return out_json(diff)
        case _:
            return 'Wrong format!\nPlease choose from stylish, plain or json'
