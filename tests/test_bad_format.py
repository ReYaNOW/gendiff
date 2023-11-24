from gendiff import generate_diff


def test_gendiff_bad_format(file1_json, file2_json):
    assert (
        generate_diff(file1_json, file2_json, format_name='avada_kedavra')
        == 'Unsupported format!\nPlease choose from stylish, plain, json'
    )
