from gendiff.utils import validate_value

INTEND = '    '


def get_lines_from_node(key: str, value, depth: int, type_: str) -> list:
    match type_:
        case 'add':
            symbol = '+'
        case 'delete':
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
    for key, v_info in diff.items():
        type_ = v_info['type']
        value = v_info['value']
        match type_:
            case 'dict':
                result.append(get_line_with_brace(depth, key, opening=True))
                result.extend(stylish(value, depth + 1))
                result.append(get_line_with_brace(depth, opening=False))
            case 'change':
                result.extend(get_lines_from_node(key, value, depth, 'delete'))
                result.extend(
                    get_lines_from_node(key, v_info['new_value'], depth, 'add')
                )
            case _:
                result.extend(get_lines_from_node(key, value, depth, type_))
    return result


def out_stylish(diff: dict):
    return "{\n" + "\n".join(stylish(diff)) + '\n}'
