import json


def check_key(result, key, f1, f2):
    if key in f1 and key in f2:
        if f1[key] == f2[key]:
            result += f"    {key}: {f1[key]}\n"
        else:
            result += f"  - {key}: {f1[key]}\n"
            result += f"  + {key}: {f2[key]}\n"
    elif key in f1 and key not in f2:
        result += f"  - {key}: {f1[key]}\n"
    elif key not in f1 and key in f2:
        result += f"  + {key}: {f2[key]}\n"
    return result


def generate_diff(file_path1: str, file_path2: str) -> str:
    result = "{\n"
    with open(file_path1) as f1, open(file_path2) as f2:
        f1 = json.load(f1)
        f2 = json.load(f2)
        overall = set(f1) | set(f2)
        overall_sorted = sorted(overall)
        for key in overall_sorted:
            result = check_key(result, key, f1, f2)
    result += '}'
    return result
