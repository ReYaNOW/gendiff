from gendiff.utils import validate_value

INTEND = '    '


def get_lines_from_node(key: str, value, depth: int, type_: str) -> list:
    match type_:
        case 'added':
            symbol = '+'
        case 'deleted':
            symbol = '-'
        case _:
            symbol = ' '

    if isinstance(value, dict):
        new_lines = [get_line_with_brace(depth, key, symbol, opening=True)]
        new_lines.extend(add_dict_without_internal_changes(value, depth + 1))
        new_lines.append(get_line_with_brace(depth, opening=False))
        return new_lines
    return [f'{(INTEND * depth)[:-2]}{symbol} {key}: {validate_value(value)}']


def add_dict_without_internal_changes(value: dict, depth: int) -> list:
    result = []
    for k, v in value.items():
        if isinstance(v, dict):
            result.append(get_line_with_brace(depth, k, opening=True))
            result.extend(add_dict_without_internal_changes(v, depth + 1))
            result.append(get_line_with_brace(depth, opening=False))
        else:
            result.append(f'{INTEND * depth}{k}: {validate_value(v)}')
    return result


def get_line_with_brace(depth: int, key=None, symbol='', opening=True) -> str:
    if opening:
        if symbol:
            return f'{(INTEND * depth)[:-2]}{symbol} {key}: ' + '{'
        return f'{INTEND * depth}{key}: ' + '{'
    return f'{INTEND * depth}' + '}'


def stylish(diff: dict, depth=1):
    result = []
    for key, key_info in diff.items():
        type_ = key_info['type']
        val = key_info['value']
        new_val = key_info.get('new_value')

        match type_:
            case 'nested':
                result.append(get_line_with_brace(depth, key, opening=True))
                result.extend(stylish(val, depth + 1))
                result.append(get_line_with_brace(depth, opening=False))
            case 'changed':
                result.extend(get_lines_from_node(key, val, depth, 'deleted'))
                result.extend(
                    get_lines_from_node(key, new_val, depth, 'added')
                )
            case _:
                result.extend(get_lines_from_node(key, val, depth, type_))
    return result


def out_stylish(diff: dict):
    return "{\n" + "\n".join(stylish(diff)) + '\n}'
