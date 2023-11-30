from gendiff import generate_diff


def test_plain_format(nested_file1_json, nested_file2_json, f1_to_f2_plain):
    assert (
        generate_diff(
            nested_file1_json, nested_file2_json, format_name='plain'
        )
        == f1_to_f2_plain
    )
