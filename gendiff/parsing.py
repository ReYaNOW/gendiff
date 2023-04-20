import yaml
import json


def parser(file, extension):
    match extension:
        case "json":
            with open(file) as file:
                return json.load(file)
        case "yaml" | "yml":
            with open(file) as file:
                return yaml.safe_load(file)


def parse_files(file_path1: str, file_path2: str) -> tuple:
    """
    This function parses two files and returns their contents.

    Args:
    - file_path1 (str): the path to the first file to be parsed.
    - file_path2 (str): the path to the second file to be parsed.

    Returns:
    - tuple: a tuple containing the contents of the two files.
    """
    f1 = parser(file_path1, file_path1.split(".")[-1])
    f2 = parser(file_path2, file_path2.split(".")[-1])
    return f1, f2
