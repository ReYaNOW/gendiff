from gendiff import generate_diff


def test_gendiff_yaml_and_json(
    big_file1_json, big_file2_yml, f1_to_f2_recursive
):
    assert generate_diff(big_file1_json, big_file2_yml) == f1_to_f2_recursive
