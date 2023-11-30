from gendiff import generate_diff


def test_gendiff_recursive(
    nested_file1_json, nested_file2_json, f1_to_f2_recursive
):
    assert (
        generate_diff(nested_file1_json, nested_file2_json)
        == f1_to_f2_recursive
    )
