from gendiff.output_formats.json import render_json
from gendiff.output_formats.plain import render_plain
from gendiff.output_formats.stylish import render_stylish


def generate_output(diff_tree: dict, format_name: str) -> str:
    match format_name:
        case 'stylish':
            return render_stylish(diff_tree)
        case 'plain':
            return render_plain(diff_tree)
        case 'json':
            return render_json(diff_tree)
        case _:
            return 'Wrong format!\nPlease choose from stylish, plain or json'
