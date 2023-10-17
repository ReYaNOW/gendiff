from gendiff import generate_diff


def test_gendiff_flat1(file1_json, file2_json, f1_to_f2):
    assert generate_diff(file1_json, file2_json) == f1_to_f2


def test_gendiff_flat2(file1_json, file2_json, f2_to_f1):
    assert generate_diff(file2_json, file1_json) == f2_to_f1
