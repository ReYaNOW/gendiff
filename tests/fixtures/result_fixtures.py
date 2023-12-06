import pytest

pytest_plugins = [
    'tests.fixtures.test_files',
    'tests.fixtures.result_fixtures',
]


@pytest.fixture
def f1_to_f2():
    with open('tests/fixtures/result_flat_f1_to_f2.txt') as file:
        return file.read()


@pytest.fixture
def f2_to_f1():
    with open('tests/fixtures/result_flat_f2_to_f1.txt') as file:
        return file.read()


@pytest.fixture
def f1_to_f2_recursive():
    with open('tests/fixtures/result_recursive.txt') as file:
        return file.read()


@pytest.fixture
def f1_to_f2_plain():
    with open('tests/fixtures/result_plain.txt') as file:
        return file.read()
