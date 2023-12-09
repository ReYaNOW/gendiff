# import json
#
# from gendiff import generate_diff
#
# from tests.fixtures.test_files import get_file_paths
# from tests.fixtures.result_fixtures import get_result
#
#
# def test_plain_format():
#     file_paths = get_file_paths('nested1', 'nested2')
#     assert generate_diff(*file_paths, format_name='plain') == get_result(
#         'result_plain'
#     )
#
#
# def test_format_json():
#     output = generate_diff(
#         *get_file_paths('nested1', 'nested2'), format_name='json'
#     )
#     # Check if a result is valid JSON
#     assert isinstance(json.loads(output), dict)
#
#
# def test_wrong_format():
#     file_paths = get_file_paths('nested1', 'nested2')
#     result = 'Unsupported format!\nPlease choose from stylish, plain, json'
#     assert generate_diff(*file_paths, format_name='avada_kedavra') == result
