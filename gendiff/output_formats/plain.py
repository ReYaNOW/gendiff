from gendiff.utils import stringify_value

FORMAT_NAME = 'plain'


def plain(diff: dict, curr_prop_path: str = '') -> list:
    result = []
    for key, v_info in diff.items():
        type_ = v_info['type']
        value = v_info['value']
        property_name = f'{curr_prop_path}{key}'

        match type_:
            case 'nested':
                result.extend(plain(value, f'{property_name}.'))
            case 'added':
                val = stringify_value(value, FORMAT_NAME)
                result.append(
                    f"Property '{property_name}' was added with value: {val}"
                )
            case 'deleted':
                result.append(f"Property '{property_name}' was removed")
            case 'changed':
                old_val = stringify_value(value, FORMAT_NAME)
                new_val = stringify_value(v_info['new_value'], FORMAT_NAME)
                result.append(
                    f"Property '{property_name}' was updated. "
                    f"From {old_val} to {new_val}"
                )
    return result


def render_plain(diff: dict) -> str:
    return '\n'.join(plain(diff))
