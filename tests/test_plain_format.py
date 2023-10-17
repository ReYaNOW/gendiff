from gendiff import generate_diff


def test_plain_format(big_file1_yaml, big_file2_json, f1_to_f2_plain):
    assert (
        generate_diff(big_file1_yaml, big_file2_json, format_name='plain')
        == f1_to_f2_plain
    )
