from gendiff.utils import validate_value

FORMAT_NAME = 'plain'


def validate_path(path: str, key) -> str:
    if path == '':
        return key
    return f'{path}.{key}'


def plain(diff: dict, current_path: str = '') -> list:
    result = []
    for key, v_info in diff.items():
        type_ = v_info['type']
        value = v_info['value']
        path = validate_path(current_path, key)

        match type_:
            case 'nested':
                result.extend(plain(value, path))
            case 'added':
                val = validate_value(value, FORMAT_NAME)
                result.append(f"Property '{path}' was added with value: {val}")
            case 'deleted':
                result.append(f"Property '{path}' was removed")
            case 'changed':
                old_val = validate_value(value, FORMAT_NAME)
                new_val = validate_value(v_info['new_value'], FORMAT_NAME)
                result.append(
                    f"Property '{path}' was updated. "
                    f"From {old_val} to {new_val}"
                )
    return result


def out_plain(diff: dict) -> str:
    return '\n'.join(plain(diff))
