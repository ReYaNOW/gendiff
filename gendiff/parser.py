import yaml
import json


def parse_data(file_path: str) -> dict:
    extension = file_path.rsplit('.', maxsplit=1)[-1]
    return read_file(file_path, extension)


def read_file(file_path: str, extension: str):
    with open(file_path) as file:
        match extension:
            case 'json':
                return json.load(file)
            case 'yaml' | 'yml':
                return yaml.safe_load(file)
