import argparse
import sys


def main():
    description = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(prog="gendiff", description=description)
    parser.add_argument(
        "first_file",
        type=str,
    )

    parser.add_argument(
        "second_file",
        type=str,
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    print(args.accumulate(args))


if __name__ == "__main__":
    main()
