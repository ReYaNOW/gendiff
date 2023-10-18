INTEND = '    '


def check_val(value) -> str:
    match value:
        case None:
            return 'null'
        case bool():
            return f'{str(value).lower()}'
        case _:
            return f'{value}'


def get_lines_from_node(key: str, value, depth: int, type_: str) -> list:
    match type_:
        case 'add':
            symbol = '+'
        case 'delete':
            symbol = '-'
        case _:
            symbol = ' '

    if isinstance(value, dict):
        return add_dict_without_internal_changes(key, value, depth, symbol)
    return [f'{(INTEND * depth)[:-2]}{symbol} {key}: {check_val(value)}']


def get_line_with_brace(
    depth: int, key=None, symbol: str = '', opening: bool = True
) -> str:
    if opening:
        if symbol:
            return f'{(INTEND * depth)[:-2]}{symbol} {key}: ' + '{'
        return f'{INTEND * depth}{key}: ' + '{'
    return f'{INTEND * depth}' + '}'


def add_dict_without_internal_changes(
    key: str, value: dict, depth: int, symbol: str
) -> list:
    def recursive_add(value, depth):
        for k, v in value.items():
            if isinstance(v, dict):
                result.append(get_line_with_brace(depth, k, opening=True))
                recursive_add(v, depth + 1)
                result.append(get_line_with_brace(depth, k, opening=False))
                continue
            result.append(f'{INTEND * depth}{k}: {check_val(v)}')

    result = [get_line_with_brace(depth, key, symbol, opening=True)]
    recursive_add(value, depth + 1)
    result.append(get_line_with_brace(depth, opening=False))
    return result


def stylish(result: list, diff: list) -> list:
    for item in diff:
        type_ = item['type']
        value = item['value']
        key = item['key']
        depth = item['depth']

        match type_:
            case 'dict':
                result.append(get_line_with_brace(depth, key, opening=True))
                stylish(result, value)
                result.append(get_line_with_brace(depth, key, opening=False))

            case 'change':
                result.extend(get_lines_from_node(key, value, depth, 'delete'))
                result.extend(
                    get_lines_from_node(key, item['new_value'], depth, 'add')
                )

            case _:
                result.extend(get_lines_from_node(key, value, depth, type_))
    return result


def out_stylish(diff: list) -> str:
    result = ['{']
    stylish(result, diff)
    result.append('}')
    return "\n".join(result)
