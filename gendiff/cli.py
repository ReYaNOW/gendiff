import argparse


def get_args_from_cli() -> argparse.Namespace:
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
    args = parser.parse_args()
    return args
