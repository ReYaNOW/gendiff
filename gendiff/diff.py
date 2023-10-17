def get_diff_with_same_keys(f1, f2, key, value, depth):
    if isinstance(f1[key], dict) and isinstance(f2[key], dict):
        return {
            'key': key,
            'value': make_diff(value, f1[key], f2[key], depth + 1),
            'type': 'dict',
            'depth': depth,
        }

    node = {'key': key, 'value': f1[key], 'type': 'keep', 'depth': depth}
    if f1[key] != f2[key]:
        node['type'] = 'change'
        node['new_value'] = f2[key]
    return node


def get_diff_with_not_same_keys(f1, f2, key, depth):
    node = {
        'key': key,
        'type': 'delete',
        'depth': depth,
    }
    if key in f1 and key not in f2:
        node['type'] = 'delete'
        node['value'] = f1[key]
        if isinstance(node['value'], dict):
            node['type'] = 'dict_delete'
    elif key not in f1 and key in f2:
        node['type'] = 'add'
        node['value'] = f2[key]
        if isinstance(node['value'], dict):
            node['type'] = 'dict_add'

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
    for k, v in general_dict.items():
        if k in f1 and k in f2:
            node = get_diff_with_same_keys(f1, f2, k, v, depth)
        else:
            node = get_diff_with_not_same_keys(f1, f2, k, depth)
        result.append(node)
    return result
