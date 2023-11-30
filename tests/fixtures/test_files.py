import pytest

pytest_plugins = [
    'tests.fixtures.test_files',
    'tests.fixtures.result_fixtures',
]


@pytest.fixture
def file1_json():
    return 'tests/fixtures/flat_file1.json'


@pytest.fixture
def file2_json():
    return 'tests/fixtures/flat_file2.json'


@pytest.fixture
def nested_file1_json():
    return 'tests/fixtures/nested_file1.json'


@pytest.fixture
def nested_file2_json():
    return 'tests/fixtures/nested_file2.json'


@pytest.fixture
def nested_file2_yml():
    return 'tests/fixtures/nested_file2.yml'
