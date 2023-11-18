import itertools

from gendiff.utils import validate_value

INTEND = '    '


def get_line(key: str, value, depth, type_=None) -> str:
    new_depth = depth + 1
    deep_indent = INTEND * new_depth

    match type_:
        case 'added':
            symbol = '+'
        case 'deleted':
            symbol = '-'
        case _:
            symbol = ' '

    return f'{deep_indent[:-2]}{symbol} {key}: {stylish(value, new_depth)}'


def stylish(current_value, depth):
    if not isinstance(current_value, dict):
        return validate_value(current_value)

    lines = []
    for key, key_info in current_value.items():
        if not isinstance(key_info, dict) or 'type' not in key_info:
            lines.append(get_line(key, key_info, depth))
            continue

        type_ = key_info['type']
        val = key_info['value']
        new_val = key_info.get('new_value')

        if type_ == 'changed':
            lines.append(get_line(key, val, depth, type_='deleted'))
            lines.append(get_line(key, new_val, depth, type_='added'))
        else:
            lines.append(get_line(key, val, depth, type_))

    current_indent = '    ' * depth
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def render_stylish(diff: dict):
    return stylish(diff, depth=0)
