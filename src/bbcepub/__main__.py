
import argparse
import sys

from bbcepub.creator import Creator
from bbcepub.utils import get_user_config, clear_temp_dirs


def main():
    print("dd")

    parser = argparse.ArgumentParser(description="conver BBC articles to .epub")
    parser.add_argument('input_path', type=str, help='an integer for the accumulator')
    args = parser.parse_args()

    print(args.input_path)
    path = args.input_path

    with open(path, "r") as f:
        print(f.readlines())
    
    clear_temp_dirs()


    # try:
    #     config = get_user_config()
    # except ValueError as e:
    #     print(e)
    #     sys.exit()
    # creator = Creator(config.title, config.urls)
    # creator.create_epub()

main()
