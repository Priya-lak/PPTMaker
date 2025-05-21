from os.path import exists
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent


def read_file(file_path: str):
    check_file_or_directory_exists(file_path)
    return open(file_path, "r").read()


def check_file_or_directory_exists(path: str):
    if not exists(path):
        raise FileNotFoundError(f"{path} not found")
    return True
