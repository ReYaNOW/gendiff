from gendiff import generate_diff
from gendiff.cli import make_parser


def main():
    parser = make_parser()
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
