import os
import shutil

from config import TEMP_DIR, TEMP_IMG_DIR


def clear_temp_dirs():
    shutil.rmtree(TEMP_DIR)
    shutil.rmtree(TEMP_IMG_DIR)
    os.mkdir(TEMP_DIR)
    os.mkdir(TEMP_IMG_DIR)
