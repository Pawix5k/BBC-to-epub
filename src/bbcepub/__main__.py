
import argparse
import sys
from pathlib import Path

from bbcepub.creator import create_epub
from bbcepub.utils import get_user_config


def main():
    parser = argparse.ArgumentParser(description="convert BBC articles to .epub")
    parser.add_argument('input_path', type=str, help='path to .txt file (1st line: .output fileaname, subsequent lines: BBC article urls)')
    args = parser.parse_args()

    try:
        name, links = get_user_config(Path(args.input_path))
    except (ValueError, FileNotFoundError) as e:
        print(e)
        sys.exit()
    
    create_epub(name, links)


main()
