import itertools


INTEND = '    '


def stringify_value(value) -> str:
    match value:
        case None:
            return 'null'
        case bool():
            return str(value).lower()
        case _:
            return f'{value}'


def render_stylish(diff: dict):
    def stylish(current_value, depth: int) -> str:
        if not isinstance(current_value, dict):
            return stringify_value(current_value)

        lines = []
        for key, key_info in current_value.items():
            if not isinstance(key_info, dict) or 'type' not in key_info:
                lines.append(generate_line(key, key_info, depth))
                continue

            type_ = key_info['type']
            val = key_info['value']
            new_val = key_info.get('new_value')

            if type_ == 'changed':
                lines.append(generate_line(key, val, depth, type_='deleted'))
                lines.append(generate_line(key, new_val, depth, type_='added'))
            else:
                lines.append(generate_line(key, val, depth, type_))

        current_indent = INTEND * depth
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    def generate_line(key: str, value, depth: int, type_=None) -> str:
        new_depth = depth + 1
        deep_indent = (INTEND * new_depth)[:-2]

        match type_:
            case 'added':
                symbol = '+'
            case 'deleted':
                symbol = '-'
            case _:
                symbol = ' '

        return f'{deep_indent}{symbol} {key}: {stylish(value, new_depth)}'

    return stylish(diff, depth=0)
