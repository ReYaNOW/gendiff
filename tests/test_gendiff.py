from gendiff import generate_diff
from gendiff.output_formats.consts import FORMATS


def get_file_paths(f1_name, f2_name):
    return f'tests/fixtures/{f1_name}.json', f'tests/fixtures/{f2_name}.json'


def get_result(result_name):
    with open(f'tests/fixtures/results/{result_name}') as file:
        return file.read()


result_flat_stylish = get_result('result_flat_stylish')
result_flat_plain = get_result('result_flat_plain')
result_flat_json = get_result('result_flat_json')


def test_gendiff_flat():
    file_paths = get_file_paths('flat1', 'flat2')
    assert generate_diff(*file_paths) == result_flat_stylish
    assert generate_diff(*file_paths, FORMATS.STYLISH) == result_flat_stylish
    assert generate_diff(*file_paths, FORMATS.PLAIN) == result_flat_plain
    assert generate_diff(*file_paths, FORMATS.JSON) == result_flat_json


result_nested_stylish = get_result('result_nested_stylish')
result_nested_plain = get_result('result_nested_plain')
result_nested_json = get_result('result_nested_json')


def test_gendiff_nested():
    file_paths = get_file_paths('nested1', 'nested2')
    assert generate_diff(*file_paths, FORMATS.STYLISH) == result_nested_stylish
    assert generate_diff(*file_paths, FORMATS.PLAIN) == result_nested_plain
    assert generate_diff(*file_paths, FORMATS.JSON) == result_nested_json


def test_gendiff_yml():
    file_paths = f'tests/fixtures/nested1.json', f'tests/fixtures/nested2.yml'
    assert generate_diff(*file_paths) == result_nested_stylish


def test_wrong_format():
    file_paths = get_file_paths('nested1', 'nested2')
    result = 'Unsupported format!\nPlease choose from stylish, plain, json'
    assert generate_diff(*file_paths, format_name='avada_kedavra') == result
