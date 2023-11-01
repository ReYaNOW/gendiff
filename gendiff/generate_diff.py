from gendiff.diff_tree import make_diff_tree
from gendiff.output_formats import generate_output
from gendiff.utils import parse_data, update_dict


def generate_diff(path1: str, path2: str, format_name: str = 'stylish') -> str:
    f1_ext = path1.rsplit('.', maxsplit=1)[-1]
    f2_ext = path2.rsplit('.', maxsplit=1)[-1]

    with open(path1) as f1, open(path2) as f2:
        f1_content, f2_content = parse_data(f1, f1_ext), parse_data(f2, f2_ext)

    overall_dict = update_dict(f1_content, f2_content)
    diff = make_diff_tree(overall_dict, f1_content, f2_content)
    return generate_output(diff, format_name)
