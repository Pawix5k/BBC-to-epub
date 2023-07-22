import json

from content import Content
from creator import Creator


def get_user_config():
    with open("user_config.json", "r") as f:
        config = json.load(f)
    return config


def main():
    config = get_user_config()
    content = Content(config["title"], config["links"])
    creator = Creator(content)
    creator.create_epub()


if __name__ == "__main__":
    main()
