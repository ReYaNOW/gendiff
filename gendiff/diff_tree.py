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
            diff[key] = {'type': 'added', 'value': validate_val(dict2[key])}
        else:
            diff[key] = {'type': 'deleted', 'value': validate_val(dict1[key])}
    return diff


def get_diff_with_same_keys(val1, val2):
    if isinstance(val1, dict) and isinstance(val2, dict):
        return {'type': 'nested', 'value': build_diff_tree(val1, val2)}
    if val1 == val2:
        return {'type': 'unchanged', 'value': validate_val(val1)}

    val1, val2 = validate_val(val1), validate_val(val2)
    return {'type': 'changed', 'value': val1, 'new_value': val2}


def validate_val(value):
    if isinstance(value, dict):
        return build_diff_tree(value, value)
    return value
