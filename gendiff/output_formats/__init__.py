from gendiff.output_formats.json_output import out_json
from gendiff.output_formats.plain import out_plain
from gendiff.output_formats.stylish import out_stylish


def generate_output(diff: list, format_name: str) -> str:
    match format_name:
        case 'stylish':
            return out_stylish(diff)
        case 'plain':
            return out_plain(diff)
        case 'json':
            return out_json(diff)
        case _:
            return 'Wrong format!\nPlease choose from stylish, plain or json'
