def make_diff_tree(dict1: dict, dict2: dict) -> dict:
    """
    Compute the difference between two given dictionaries,
    and return a dict of changes made.
    """
    keys = dict1.keys() | dict2.keys()

    diff = {}
    for key in sorted(keys):
        if key in dict1 and key in dict2:
            diff[key] = get_diff_with_same_keys(dict1[key], dict2[key])
        elif key not in dict1:
            diff[key] = {'type': 'added', 'value': dict2[key]}
        else:
            diff[key] = {'type': 'deleted', 'value': dict1[key]}
    return diff


def get_diff_with_same_keys(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return {'type': 'nested', 'value': make_diff_tree(dict1, dict2)}
    if dict1 == dict2:
        return {'type': 'kept', 'value': dict1}
    return {'type': 'changed', 'value': dict1, 'new_value': dict2}
