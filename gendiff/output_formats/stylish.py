from gendiff.output_formats.consts import INDENT


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
        for k, key_info in current_value.items():
            match key_info:
                case {'type': 'added', 'value': add_v}:
                    lines.append(generate_line(k, add_v, depth, symbol='+'))

                case {'type': 'deleted', 'value': del_v}:
                    lines.append(generate_line(k, del_v, depth, symbol='-'))

                case {'type': 'changed', 'value': old_v, 'new_value': new_v}:
                    lines.append(generate_line(k, old_v, depth, symbol='-'))
                    lines.append(generate_line(k, new_v, depth, symbol='+'))

                case {'type': 'nested'} | {'type': 'unchanged'}:
                    value = key_info['value']
                    lines.append(generate_line(k, value, depth, symbol=' '))

                case _:
                    lines.append(generate_line(k, key_info, depth, symbol=' '))

        closing_bracket = f'{INDENT * depth}}}'
        lines = '\n'.join(lines)
        return f'{{\n{lines}\n{closing_bracket}'

    def generate_line(key, value, depth, symbol):
        new_depth = depth + 1
        deep_indent = (INDENT * new_depth)[:-2]
        return f'{deep_indent}{symbol} {key}: {stylish(value, new_depth)}'

    return stylish(diff, depth=0)
