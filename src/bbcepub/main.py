import sys

from creator import Creator
from utils import get_user_config


def main():
    try:
        config = get_user_config()
    except ValueError as e:
        print(e)
        sys.exit()
    creator = Creator(config.title, config.urls)
    creator.create_epub()


if __name__ == "__main__":
    main()
