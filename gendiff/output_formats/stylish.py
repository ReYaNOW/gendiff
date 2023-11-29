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
            val = key_info['value']
            new_v = key_info.get('new_value')

            match key_info['type']:
                case 'added':
                    lines.append(generate_line(k, val, depth, symbol='+'))

                case 'deleted':
                    lines.append(generate_line(k, val, depth, symbol='-'))

                case 'changed':
                    lines.append(generate_line(k, val, depth, symbol='-'))
                    lines.append(generate_line(k, new_v, depth, symbol='+'))

                case _:
                    lines.append(generate_line(k, val, depth, symbol=' '))

        closing_bracket = f'{INDENT * depth}}}'
        lines = '\n'.join(lines)
        return f'{{\n{lines}\n{closing_bracket}'

    def generate_line(key: str, value, depth: int, symbol: str):
        new_depth = depth + 1
        deep_indent = (INDENT * new_depth)[:-2]
        return f'{deep_indent}{symbol} {key}: {stylish(value, new_depth)}'

    return stylish(diff, depth=0)
