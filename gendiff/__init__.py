from gendiff.scripts.parsing import parse_files


def bool_lower(key, file):
    if isinstance(file[key], bool):
        return str(file[key]).lower()
    else:
        return file[key]


def check_same_key(result, key, f1, f2):
    if f1[key] == f2[key]:
        result += f"    {key}: {bool_lower(key, f1)}\n"
    else:
        result += f"  - {key}: {bool_lower(key, f1)}\n"
        result += f"  + {key}: {bool_lower(key, f2)}\n"
    return result


def check_key(result, key, f1, f2):
    if key in f1 and key in f2:
        result = check_same_key(result, key, f1, f2)
    elif key in f1 and key not in f2:
        result += f"  - {key}: {bool_lower(key, f1)}\n"
    elif key not in f1 and key in f2:
        result += f"  + {key}: {bool_lower(key, f2)}\n"
    return result


def generate_diff(file_path1: str, file_path2: str) -> str:
    result = "{\n"
    f1, f2 = parse_files(file_path1, file_path2)
    overall = set(f1) | set(f2)
    overall_sorted = sorted(overall)
    for key in overall_sorted:
        result = check_key(result, key, f1, f2)
    result += '}'
    return result
