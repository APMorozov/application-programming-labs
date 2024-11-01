import argparse

DEFAULT_DIR_PATH = "images"
DEFAULT_CSV_PATH = "annotation.csv"


def args_parser() -> str:
    """
    Parce args from command line
    :return: Class Object Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path to csv file",
        type=str,
        help="Path to csv file.")
    arg = parser.parse_args()
    return arg
