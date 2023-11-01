from gendiff import generate_diff
from gendiff.cli import parse_args_from_cli


def main():
    args = parse_args_from_cli()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
