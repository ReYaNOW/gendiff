import json

import pytest

from gendiff import generate_diff


@pytest.fixture
def f1_to_f2_format_json(big_file1_json, big_file2_json):
    return generate_diff(big_file1_json, big_file2_json, format_name='json')


def test_format_json(f1_to_f2_format_json):
    # Check if a result is valid JSON

    assert isinstance(json.loads(f1_to_f2_format_json), list)
