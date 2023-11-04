from gendiff.diff_tree import make_diff_tree
from gendiff.output_formats import generate_output
from gendiff.parser import parse_data
from gendiff.utils import update_dict


def get_content_from_file(path):
    extension = path.rsplit('.', maxsplit=1)[-1]

    with open(path) as file:
        file_content = parse_data(file, extension)
        return file_content


def generate_diff(path1: str, path2: str, format_name: str = 'stylish') -> str:
    f1_content = get_content_from_file(path1)
    f2_content = get_content_from_file(path2)

    overall_dict = update_dict(f1_content, f2_content)
    diff = make_diff_tree(overall_dict, f1_content, f2_content)
    return generate_output(diff, format_name)
