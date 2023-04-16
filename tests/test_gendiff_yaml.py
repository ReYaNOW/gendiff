from gendiff import generate_diff
import pytest


@pytest.fixture
def result_f1_to_f2_in_yaml():
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
def result_f2_to_f1_in_yaml():
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


def test_gendiff_flat_yaml1(file1_yaml, file2_yml, result_f1_to_f2_in_yaml):
    assert generate_diff(file1_yaml, file2_yml) == result_f1_to_f2_in_yaml


def test_gendiff_flat_yaml2(file2_yml, file1_yaml, result_f2_to_f1_in_yaml):
    assert generate_diff(file2_yml, file1_yaml) == result_f2_to_f1_in_yaml
