def get_file_paths(f1_name, f2_name):
    e1, e2 = get_file_ext(f1_name), get_file_ext(f2_name)
    return f'tests/fixtures/{f1_name}.{e1}', f'tests/fixtures/{f2_name}.{e2}'


def get_file_ext(file_name):
    if 'yml' in file_name:
        ext = 'yml'
    elif 'yaml' in file_name:
        ext = 'yaml'
    else:
        ext = 'json'
    return ext
