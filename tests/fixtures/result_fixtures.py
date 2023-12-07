def get_result(result_name):
    with open(f'tests/fixtures/{result_name}.txt') as file:
        return file.read()
