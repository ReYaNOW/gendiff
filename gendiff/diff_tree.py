def get_diff_with_same_keys(f1, f2, key, value, depth):
    if isinstance(f1[key], dict) and isinstance(f2[key], dict):
        return {
            'key': key,
            'value': make_diff_tree(value, f1[key], f2[key], depth + 1),
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


def make_diff_tree(general_dict: dict, f1: dict, f2: dict, depth=1) -> list:
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
