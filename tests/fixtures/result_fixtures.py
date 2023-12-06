import pytest


def get_result(result_name):
    with open(f'tests/fixtures/{result_name}.txt') as file:
        return file.read()


@pytest.fixture
def f1_to_f2():
    with open('tests/fixtures/result_flat1.txt') as file:
        return file.read()


@pytest.fixture
def f2_to_f1():
    with open('tests/fixtures/result_flat2.txt') as file:
        return file.read()


@pytest.fixture
def f1_to_f2_recursive():
    with open('tests/fixtures/result_recursive.txt') as file:
        return file.read()


@pytest.fixture
def f1_to_f2_plain():
    with open('tests/fixtures/result_plain.txt') as file:
        return file.read()
