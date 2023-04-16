from gendiff import generate_diff
import pytest
import json


@pytest.fixture
def f1_to_f2_format_json(big_file1_yaml, big_file2_yml):
    return generate_diff(big_file1_yaml, big_file2_yml, format_name="json")


def test_format_json(f1_to_f2_format_json):
    # Check if a result is valid JSON

    assert isinstance(json.loads(f1_to_f2_format_json), list)
