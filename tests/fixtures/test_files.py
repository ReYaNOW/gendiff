import pytest

pytest_plugins = [
    "tests.fixtures.test_files",
]


@pytest.fixture
def file1_json():
    return "tests/fixtures/file1.json"


@pytest.fixture
def file2_json():
    return "tests/fixtures/file2.json"


@pytest.fixture
def file1_yaml():
    return "tests/fixtures/file1.yaml"


@pytest.fixture
def file2_yaml():
    return "tests/fixtures/file2.yml"
