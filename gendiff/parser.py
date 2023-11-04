from typing import IO

import json
import yaml


def parse_data(file: IO, file_format: str) -> dict:
    match file_format:
        case 'json':
            return json.load(file)
        case 'yaml' | 'yml':
            return yaml.safe_load(file)
        case _:
            raise ValueError(f'Unsupported file format: {file_format}')
