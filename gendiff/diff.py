from copy import deepcopy

from gendiff.parsers.file_parser import parse_file


def get_diff_with_same_keys(f1, f2, key, value, depth):
    if isinstance(f1[key], dict) and isinstance(f2[key], dict):
        return {
            'key': key,
            'value': make_diff(value, f1[key], f2[key], depth + 1),
            'type': 'dict',
            'depth': depth,
        }

    node = {
        'key': key,
        'value': f1[key],
        'type': 'keep',
        'depth': depth,
    }
    if f1[key] != f2[key]:
        node['type'] = 'change'
        node['new_value'] = f2[key]
    return node


def make_diff(general_dict: dict, f1: dict, f2: dict, depth=1) -> list:
    """
    Compute the difference between two given dictionaries,
    and return a list of changes made.

    args:
        general_dict (dict): the general dictionary
        that contains both f1 and f2
        f1 (dict): the first dictionary to be compared
        f2 (dict): the second dictionary to be compared to f1
        depth (int): the level of depth in the dictionary
        being currently compared, default at 1

    return:
        A list of dictionary items that represent the differences between
        f1 and f2. A dictionary item represents a specific change.
    """
    general_dict = dict(sorted(general_dict.items()))
    result = []
    for key, value in general_dict.items():
        if key in f1 and key in f2:
            node = get_diff_with_same_keys(f1, f2, key, value, depth)
        else:
            node = {
                'key': key,
                'type': 'delete',
                'depth': depth,
            }
            if key in f1 and key not in f2:
                node['type'] = 'delete'
                node['value'] = f1[key]
            elif key not in f1 and key in f2:
                node['type'] = 'add'
                node['value'] = f2[key]
        result.append(node)
    return result


def update(f1: dict, f2: dict) -> dict:
    for k, v in f2.items():
        if not isinstance(f1, dict):
            f1 = f2
        elif isinstance(v, dict):
            r = update(f1.get(k, {}), v)
            f1[k] = r
        else:
            f1[k] = f2[k]
    return f1


def get_diff(path1: str, path2: str) -> list:
    f1_content, f2_content = parse_file(path1), parse_file(path2)
    overall = update(deepcopy(f1_content), deepcopy(f2_content))

    diff = make_diff(overall, f1_content, f2_content)
    return diff
