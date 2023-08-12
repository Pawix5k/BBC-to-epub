
import argparse
import sys
import os
from pathlib import Path

from bbcepub.creator import create_epub
from bbcepub.utils import get_user_config


def main():
    print("dd")

    parser = argparse.ArgumentParser(description="convert BBC articles to .epub")
    parser.add_argument('input_path', type=str, help='an integer for the accumulator')
    args = parser.parse_args()

    print(args.input_path)

    name, links = get_user_config(Path(args.input_path))
    
    create_epub(name, links)



    # try:
    #     config = get_user_config()
    # except ValueError as e:
    #     print(e)
    #     sys.exit()
    # creator = Creator(config.title, config.urls)
    # creator.create_epub()

main()
