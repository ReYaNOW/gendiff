from typing import IO

import json
import yaml


def parse_data(data: IO, data_format: str) -> dict:
    match data_format:
        case 'json':
            return json.load(data)
        case 'yaml' | 'yml':
            return yaml.safe_load(data)
        case _:
            raise ValueError(f'Unsupported data format: {data_format}')
