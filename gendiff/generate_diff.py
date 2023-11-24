from gendiff.diff_tree import build_diff_tree
from gendiff.output_formats import generate_output
from gendiff.parser import parse_data
from gendiff.consts import FORMATS


def get_extension_from_path(path: str) -> str:
    return path.rsplit('.', maxsplit=1)[-1].lower()


def get_data_from_file(path: str) -> dict:
    extension = get_extension_from_path(path)

    with open(path) as file:
        return parse_data(file, extension)


def generate_diff(
    path1: str, path2: str, format_name: str = FORMATS.STYLISH
) -> str:
    f1_data = get_data_from_file(path1)
    f2_data = get_data_from_file(path2)

    diff = build_diff_tree(f1_data, f2_data)
    return generate_output(diff, format_name)
