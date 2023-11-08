from typing import IO

import json
import yaml


def parse_data(file: IO, data_format: str) -> dict:
    match data_format:
        case 'json':
            return json.load(file)
        case 'yaml' | 'yml':
            return yaml.safe_load(file)
        case _:
            raise ValueError(f'Unsupported file format: {data_format}')
