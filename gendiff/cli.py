import argparse


def make_parser() -> argparse.ArgumentParser:
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(prog='gendiff', description=description)
    parser.add_argument(
        'first_file',
        type=str,
    )

    parser.add_argument(
        'second_file',
        type=str,
    )

    help_ = 'set format of output (stylish, plain or json), default is stylish'
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help=help_,
        type=str,
    )
    return parser
