import argparse


def parse_args() -> argparse.Namespace:
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(prog='gendiff', description=description)

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output (stylish, plain, json), default is stylish',
    )
    return parser.parse_args()
