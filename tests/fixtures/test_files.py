import pytest

pytest_plugins = [
    'tests.fixtures.test_files',
    'tests.fixtures.result_fixtures',
]


@pytest.fixture
def file1_json():
    return 'tests/fixtures/flat1.json'


@pytest.fixture
def file2_json():
    return 'tests/fixtures/flat2.json'


@pytest.fixture
def nested_file1_json():
    return 'tests/fixtures/nested1.json'


@pytest.fixture
def nested_file2_json():
    return 'tests/fixtures/nested2.json'


@pytest.fixture
def nested_file2_yml():
    return 'tests/fixtures/nested2.yml'
