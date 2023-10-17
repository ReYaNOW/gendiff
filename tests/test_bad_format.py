from gendiff import generate_diff


def test_gendiff_flat1(file1_json, file2_json):
    assert (
        generate_diff(file1_json, file2_json, format_name='avada_kedavra')
        == 'Wrong format!\nPlease choose from stylish, plain or json'
    )
