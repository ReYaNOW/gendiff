from gendiff import generate_diff
import pytest


@pytest.fixture
def file1():
    return "tests/fixtures/file1.json"


@pytest.fixture
def file2():
    return "tests/fixtures/file2.json"


@pytest.fixture
def result_f1_to_f2():
    return "\n".join(
        [
            "{",
            "  - follow: False",
            "    host: hexlet.io",
            "  - proxy: 123.234.53.22",
            "  - timeout: 50",
            "  + timeout: 20",
            "  + verbose: True",
            "}",
        ]
    )


@pytest.fixture
def result_f2_to_f1():
    return "\n".join(
        [
            "{",
            "  + follow: False",
            "    host: hexlet.io",
            "  + proxy: 123.234.53.22",
            "  - timeout: 20",
            "  + timeout: 50",
            "  - verbose: True",
            "}",
        ]
    )


def test_gendiff_flat1(file1, file2, result_f1_to_f2):
    assert generate_diff(file1, file2) == result_f1_to_f2


def test_gendiff_flat2(file2, file1, result_f2_to_f1):
    assert generate_diff(file2, file1) == result_f2_to_f1
