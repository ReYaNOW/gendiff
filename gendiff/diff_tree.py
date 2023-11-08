def make_diff_tree(dict1: dict, dict2: dict) -> dict:
    """
    Compute the difference between two given dictionaries,
    and return a dict of changes made.
    """
    keys = dict1.keys() | dict2.keys()
    keys = sorted(keys)

    diff = {}
    for key in keys:
        if key in dict1 and key in dict2:
            diff[key] = get_diff_with_same_keys(dict1[key], dict2[key])
        else:
            if key not in dict1:
                diff[key] = {'type': 'add', 'value': dict2[key]}
            else:
                diff[key] = {'type': 'delete', 'value': dict1[key]}
    return diff


def get_diff_with_same_keys(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return {'type': 'dict', 'value': make_diff_tree(dict1, dict2)}
    if dict1 == dict2:
        return {'type': 'keep', 'value': dict1}
    return {'type': 'change', 'value': dict1, 'new_value': dict2}
