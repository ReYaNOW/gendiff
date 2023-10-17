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
        match f1:
            case {} if k in f1 and k in f2:
                if isinstance(f1[k], dict) and isinstance(f2[k], dict):
                    result.append(
                        {
                            'key': k,
                            'value': make_diff(v, f1[k], f2[k], depth + 1),
                            'type': 'dict',
                            'depth': depth,
                        }
                    )
                else:
                    current = {
                        'key': k,
                        'value': f1[k],
                        'type': 'keep',
                        'depth': depth,
                    }
                    if f1[k] != f2[k]:
                        current['type'] = 'change'
                        current['old_value'] = current.pop("value")
                        current['new_value'] = f2[k]
                    result.append(current)
            case _:
                current = {
                    'key': k,
                    'type': 'delete',
                    'depth': depth,
                }
                if k in f1 and k not in f2:
                    current['type'] = 'delete'
                    current['value'] = f1[k]
                    if isinstance(current['value'], dict):
                        current['type'] = 'dict_delete'
                elif k not in f1 and k in f2:
                    current['type'] = 'add'
                    current['value'] = f2[k]
                    if isinstance(current['value'], dict):
                        current['type'] = 'dict_add'
                result.append(current)
    return result
