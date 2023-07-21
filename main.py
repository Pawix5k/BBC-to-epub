import json

from content import Content


def get_user_config():
    with open("user_config.json", "r") as f:
        config = json.load(f)
    return config


if __name__ == "__main__":
    config = get_user_config()
    content = Content(config["title"], config["links"])
