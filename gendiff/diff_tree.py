def build_diff_tree(dict1: dict, dict2: dict) -> dict:
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
            diff[key] = get_diff_with_not_same_keys(dict2[key], 'added')
        else:
            diff[key] = get_diff_with_not_same_keys(dict1[key], 'deleted')
    return diff


def get_diff_with_same_keys(val1, val2):
    if isinstance(val1, dict) and isinstance(val2, dict):
        return {'type': 'nested', 'value': build_diff_tree(val1, val2)}
    if val1 == val2:
        return {'type': 'unchanged', 'value': val1}
    return {'type': 'changed', 'value': val1, 'new_value': val2}


def get_diff_with_not_same_keys(value, type_):
    if isinstance(value, dict):
        return {'type': type_, 'value': build_diff_tree(value, value)}
    return {'type': type_, 'value': value}
