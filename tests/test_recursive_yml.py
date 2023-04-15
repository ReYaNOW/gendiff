from gendiff import generate_diff

import pytest


@pytest.fixture
def f1_to_f2_in_json_recursive():
    return "\n".join(
        [
            "{",
            "    common: {",
            "      + follow: false",
            "        setting1: Value 1",
            "      - setting2: 200",
            "      - setting3: true",
            "      + setting3: null",
            "      + setting4: blah blah",
            "      + setting5: {",
            "            key5: value5",
            "        }",
            "        setting6: {",
            "            doge: {",
            "              - wow:",
            "              + wow: so much",
            "            }",
            "            key: value",
            "          + ops: vops",
            "        }",
            "    }",
            "    group1: {",
            "      - baz: bas",
            "      + baz: bars",
            "        foo: bar",
            "      - nest: {",
            "            key: value",
            "        }",
            "      + nest: str",
            "    }",
            "  - group2: {",
            "        abc: 12345",
            "        deep: {",
            "            id: 45",
            "        }",
            "    }",
            "  + group3: {",
            "        deep: {",
            "            id: {",
            "                number: 45",
            "            }",
            "        }",
            "        fee: 100500",
            "    }",
            "}",
        ]
    )


def test_gendiff_recursive(
    big_file1_yaml, big_file2_yml, f1_to_f2_in_json_recursive
):
    assert (
        generate_diff(big_file1_yaml, big_file2_yml)
        == f1_to_f2_in_json_recursive
    )
