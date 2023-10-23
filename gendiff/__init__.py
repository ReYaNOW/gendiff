from gendiff.get_diff import get_diff
from gendiff.output_formats.json_output import out_json
from gendiff.output_formats.plain import out_plain
from gendiff.output_formats.stylish import out_stylish


def generate_diff(path1: str, path2: str, format_name: str = 'stylish') -> str:
    """
    Generate the difference between two files.

    Args:
        path1 (str): the path to the first file to be compared.
        path2 (str): the path to the second file to be compared.
        format_name (str): the format to output the result in.
            Default is "stylish", options are "stylish", "plain" or "json".
    """
    diff = get_diff(path1, path2)
    match format_name:
        case 'stylish':
            return out_stylish(diff)
        case 'plain':
            return out_plain(diff)
        case 'json':
            return out_json(diff)
        case _:
            return 'Wrong format!\nPlease choose from stylish, plain or json'
