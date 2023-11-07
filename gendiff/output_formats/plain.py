from gendiff.utils import validate_value

FORMAT_NAME = 'plain'


def check_path(path: str, key) -> str:
    if path == '':
        return key
    return f'{path}.{key}'


def plain(result: list, diff: dict, current_path: str = '') -> list:
    for key, v in diff.items():
        type_ = v['type']
        value = v['value']
        match type_:
            case 'dict':
                plain(result, value, check_path(current_path, key))
            case 'add':
                path = check_path(current_path, key)
                val = validate_value(value, FORMAT_NAME)
                result.append(f"Property '{path}' was added with value: {val}")
            case 'delete':
                path = check_path(current_path, key)
                result.append(f"Property '{path}' was removed")
            case 'change':
                path = check_path(current_path, key)
                old_val = validate_value(value, FORMAT_NAME)
                new_val = validate_value(v['new_value'], FORMAT_NAME)
                result.append(
                    f"Property '{path}' was updated. "
                    f"From {old_val} to {new_val}"
                )
    return result


def out_plain(diff: dict) -> str:
    return '\n'.join(plain([], diff))
