def make_diff_tree(dict1: dict, dict2: dict) -> dict:
    """
    Compute the difference between two given dictionaries,
    and return a list of changes made.

    args:
        dict1 (dict): the first dictionary to be compared

        dict2 (dict): the second dictionary to be compared to dict1
    """
    same_keys = dict1.keys() & dict2.keys()
    added_keys = dict2.keys() - dict1.keys()
    deleted_keys = dict1.keys() - dict2.keys()

    diff = {}
    for key in same_keys:
        diff[key] = get_diff_with_same_keys(dict1[key], dict2[key])
    for key in added_keys:
        diff[key] = {'type': 'add', 'value': dict2[key]}
    for key in deleted_keys:
        diff[key] = {'type': 'delete', 'value': dict1[key]}
    diff = dict(sorted(diff.items()))
    return diff


def get_diff_with_same_keys(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return {'type': 'dict', 'value': make_diff_tree(dict1, dict2)}
    if dict1 == dict2:
        return {'type': 'keep', 'value': dict1}
    return {'type': 'change', 'value': dict1, 'new_value': dict2}
