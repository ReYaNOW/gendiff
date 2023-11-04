from copy import deepcopy


def update_dict(dict1: dict, dict2: dict) -> dict:
    """recursively update a dictionary with another dictionary"""

    def update(dict1, dict2):
        for k, v in dict2.items():
            if not isinstance(dict1, dict):
                dict1 = dict2
            elif isinstance(v, dict):
                r = update(dict1.get(k, {}), v)
                dict1[k] = r
            else:
                dict1[k] = dict2[k]
        return dict1

    return update(deepcopy(dict1), deepcopy(dict2))
