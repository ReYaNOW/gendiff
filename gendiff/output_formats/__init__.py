from collections import namedtuple

from gendiff.output_formats.json import render_json
from gendiff.output_formats.plain import render_plain
from gendiff.output_formats.stylish import render_stylish

_FORMAT_VALUES = ('stylish', 'plain', 'json')
FORMATS = namedtuple('FormatChoices', map(str.upper, _FORMAT_VALUES))(
    *_FORMAT_VALUES
)


def generate_output(diff_tree: dict, format_name: str) -> str:
    match format_name:
        case FORMATS.STYLISH:
            return render_stylish(diff_tree)
        case FORMATS.PLAIN:
            return render_plain(diff_tree)
        case FORMATS.JSON:
            return render_json(diff_tree)
        case _:
            return f'Wrong format!\nPlease choose from {", ".join(FORMATS)}'
