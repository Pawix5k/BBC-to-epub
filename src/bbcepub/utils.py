from collections import namedtuple
import os
import shutil
import sys

from bbcepub.config import USER_INPUT_PATH, TEMP_DIR, TEMP_IMG_DIR


def read_user_input(input_path):
    try:
        with open(input_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Required 'user_input.txt' file not found")
        sys.exit()
    return lines


def get_user_config(input_path):
    lines = read_user_input(input_path)
    if len(lines) < 1:
        raise ValueError(rf"No title or article urls specified in '{USER_INPUT_PATH}'")
    if len(lines) < 2:
        raise ValueError(rf"No article urls specified in '{USER_INPUT_PATH}'")
    if len(lines) > 101:
        raise ValueError(rf"Too many urls specified in '{USER_INPUT_PATH}' (max 100)")
    title = lines[0].strip()
    urls = [url.strip() for url in lines[1:]]
    return title, urls


def clear_temp_dirs():
    shutil.rmtree(TEMP_DIR)
    shutil.rmtree(TEMP_IMG_DIR)
    os.mkdir(TEMP_DIR)
    os.mkdir(TEMP_IMG_DIR)
