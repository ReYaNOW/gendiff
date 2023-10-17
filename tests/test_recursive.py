from gendiff import generate_diff


def test_gendiff_recursive_json(
    big_file1_json, big_file2_json, f1_to_f2_recursive
):
    assert generate_diff(big_file1_json, big_file2_json) == f1_to_f2_recursive
