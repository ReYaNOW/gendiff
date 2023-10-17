def check_val(value):
    match value:
        case None:
            return ' null'
        case bool():
            return f' {str(value).lower()}'
        case _:
            return f' {value}'


def add_dict_without_internal_changes(key, value, intend, depth, symbol):
    def recursive_add(value, depth=1):
        if not isinstance(value, dict):
            return f'{check_val(value)}'

        for k, v in value.items():
            if isinstance(v, dict):
                result.append(f'{intend * depth}{k}: ' + '{')
                recursive_add(v, depth + 1)
                result.append(f'{intend * depth}' + '}')
                continue
            result.append(f'{intend * depth}{k}:{recursive_add(v, depth)}')

    result = [f'{(intend * depth)[:-2]}{symbol} {key}: ' + '{']
    recursive_add(value, depth + 1)
    result.append(f'{(intend * depth)}' + '}')
    return result


def get_lines(key, value, intend, depth, type_):
    match type_:
        case 'add':
            symbol = '+'
        case 'delete':
            symbol = '-'
        case _:
            symbol = ' '

    if isinstance(value, dict):
        return add_dict_without_internal_changes(
            key, value, intend, depth, symbol
        )
    return [f'{(intend * depth)[:-2]}{symbol} {key}:{check_val(value)}']


def stylish(result: list, diff, intend='    '):
    for item in diff:
        type_ = item['type']
        key = item['key']
        depth = item['depth']

        match item['type']:
            case 'dict':
                result.append(f'{intend * depth}{key}: ' + "{")
                stylish(result, item['value'])
                result.append(f'{intend * depth}' + '}')

            case 'keep' | 'add' | 'delete':
                result.extend(
                    get_lines(key, item['value'], intend, depth, type_)
                )

            case 'change':
                result.extend(
                    get_lines(key, item['value'], intend, depth, 'delete')
                )
                result.extend(
                    get_lines(key, item['new_value'], intend, depth, 'add')
                )
            case 'dict_delete':
                new_lines = add_dict_without_internal_changes(
                    key, item['value'], intend, depth, '-'
                )
                result.extend(new_lines)
            case 'dict_add':
                new_lines = add_dict_without_internal_changes(
                    key, item['value'], intend, depth, '+'
                )
                result.extend(new_lines)
    return result


def out_stylish(diff: list) -> str:
    result = ['{']
    stylish(result, diff)
    result.append('}')
    return "\n".join(result)
