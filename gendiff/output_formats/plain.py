def path_check(path, key):
    if path == '':
        return key
    return f'{path}.{key}'


def dict_check(value):
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
            return f'\'{value}\''


def plain(result, diff, path='', prp='Property '):
    for item in diff:
        key = item['key']
        match item['type']:
            case 'dict':
                plain(result, item['value'], path_check(path, key))
            case 'add' | 'dict_add':
                words = ' was added with value:'
                current_path = path_check(path, key)
                v = dict_check(item['value'])
                result.append(f"{prp}'{current_path}'{words} {v}")
            case 'delete' | 'dict_delete':
                current_path = path_check(path, key)
                result.append(f"{prp}'{current_path}' was removed")
            case 'change':
                words = ' was updated. From'
                current_path = path_check(path, key)
                o_v = dict_check(item['value'])
                n_v = dict_check(item['new_value'])
                result.append(f"{prp}'{current_path}'{words} {o_v} to {n_v}")
    return result


def out_plain(diff: list) -> str:
    return '\n'.join(plain([], diff))
