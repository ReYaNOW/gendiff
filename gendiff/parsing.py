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
    f1 = parser(file_path1, file_path1.split(".")[-1])
    f2 = parser(file_path2, file_path2.split(".")[-1])
    return f1, f2
