def check_path(path: str, key) -> str:
    if path == '':
        return key
    return f'{path}.{key}'


def check_value(value) -> str:
    match value:
        case dict():
            return '[complex value]'
        case None:
            return 'null'
        case bool():
            return str(value).lower()
        case int():
            return value
        case _:
            return f"'{value}'"


def plain(result: list, diff: list, current_path: str = '') -> list:
    for item in diff:
        key = item['key']
        match item['type']:
            case 'dict':
                plain(result, item['value'], check_path(current_path, key))
            case 'add':
                path = check_path(current_path, key)
                val = check_value(item['value'])
                result.append(f"Property '{path}' was added with value: {val}")
            case 'delete':
                path = check_path(current_path, key)
                result.append(f"Property '{path}' was removed")
            case 'change':
                path = check_path(current_path, key)
                old_val = check_value(item['value'])
                new_val = check_value(item['new_value'])
                result.append(
                    f"Property '{path}' was updated. "
                    f"From {old_val} to {new_val}"
                )
    return result


def out_plain(diff: list) -> str:
    return '\n'.join(plain([], diff))
