from gendiff import generate_diff

import pytest


@pytest.fixture
def f1_to_f2_in_json():
    return "\n".join(
        [
            "Property 'common.follow' was added with value: false",
            "Property 'common.setting2' was removed",
            "Property 'common.setting3' was updated. From true to null",
            "Property 'common.setting4' was added with value: 'blah blah'",
            "Property 'common.setting5' was added with value: [complex value]",
            "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'",  # noqa  e501
            "Property 'common.setting6.ops' was added with value: 'vops'",
            "Property 'group1.baz' was updated. From 'bas' to 'bars'",
            "Property 'group1.nest' was updated. From [complex value] to 'str'",  # noqa  e501
            "Property 'group2' was removed",
            "Property 'group3' was added with value: [complex value]",
        ]
    )


def test_gendiff_flat1(big_file1_yaml, big_file2_json, f1_to_f2_in_json):
    assert generate_diff(big_file1_yaml, big_file2_json, format_name='plain') == f1_to_f2_in_json  # noqa  e501
