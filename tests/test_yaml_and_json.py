from gendiff import generate_diff

import pytest


@pytest.fixture
def f1_to_f2_in_json():
    return "\n".join(
        [
            "{",
            "  - follow: false",
            "    host: hexlet.io",
            "  - proxy: 123.234.53.22",
            "  - timeout: 50",
            "  + timeout: 20",
            "  + verbose: true",
            "}",
        ]
    )


@pytest.fixture
def f2_to_f1_in_json():
    return "\n".join(
        [
            "{",
            "  + follow: false",
            "    host: hexlet.io",
            "  + proxy: 123.234.53.22",
            "  - timeout: 20",
            "  + timeout: 50",
            "  - verbose: true",
            "}",
        ]
    )


def test_gendiff_yaml_and_json1(file1_json, file2_yml, f1_to_f2_in_json):
    assert generate_diff(file1_json, file2_yml) == f1_to_f2_in_json


def test_gendiff_flat2(file1_yaml, file2_json, f2_to_f1_in_json):
    assert generate_diff(file2_json, file1_yaml) == f2_to_f1_in_json
