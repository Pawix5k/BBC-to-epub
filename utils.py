from collections import namedtuple
import os
import shutil
import sys

from config import USER_INPUT_PATH, TEMP_DIR, TEMP_IMG_DIR


def read_user_input():
    try:
        with open(USER_INPUT_PATH, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Required 'user_input.txt' file not found")
        sys.exit()
    return lines


def get_user_config():
    lines = read_user_input()
    if len(lines) < 1:
        raise ValueError(rf"No title or article urls specified in '{USER_INPUT_PATH}'")
    if len(lines) < 2:
        raise ValueError(rf"No article urls specified in '{USER_INPUT_PATH}'")
    if len(lines) > 101:
        raise ValueError(rf"Too many urls specified in '{USER_INPUT_PATH}' (max 100)")
    UserConfig = namedtuple('UserConfig', ["title", "urls"])
    title = lines[0].strip()
    urls = [url.strip() for url in lines[1:]]
    user_config = UserConfig(title, urls)
    return user_config


def clear_temp_dirs():
    shutil.rmtree(TEMP_DIR)
    shutil.rmtree(TEMP_IMG_DIR)
    os.mkdir(TEMP_DIR)
    os.mkdir(TEMP_IMG_DIR)
