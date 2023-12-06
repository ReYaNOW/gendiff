import pytest

from gendiff import generate_diff

from tests.fixtures.test_files import get_file_paths
from tests.fixtures.result_fixtures import get_result

test_params = [
    (get_file_paths('flat1', 'flat2'), get_result('result_flat1')),
    (get_file_paths('flat2', 'flat1'), get_result('result_flat2')),
    (get_file_paths('nested1', 'nested2'), get_result('result_recursive')),
    (get_file_paths('nested1', 'nested2_yml'), get_result('result_recursive')),
]


@pytest.mark.parametrize('file_paths,expected', test_params)
def test_gendiff(file_paths, expected):
    assert generate_diff(*file_paths) == expected
