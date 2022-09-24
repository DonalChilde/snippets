import hashlib
from pathlib import Path

import pytest
from utilities.file_hash import get_file_hash, get_file_hash_generator


def test_open_type():
    file_path = Path(
        "/home/chad/projects/utilities/tests/utilities/test_function_register.py"
    )
    with open(file_path, "rb") as binary_read:
        print(type(binary_read))
    with open(file_path, "r") as binary_read:
        print(type(binary_read))


def test_hashlib_type():
    hash_lib = hashlib.md5()
    print(type(hash_lib))
    hash_lib = hashlib.blake2b()
    print(type(hash_lib))


def test_guarantee_hashers():
    hashers = hashlib.algorithms_guaranteed
    print(hashers)


def test_file_hash():
    file_path = Path(
        "/home/chad/projects/utilities/tests/utilities/test_function_register.py"
    )
    hash_str = get_file_hash(file_path, hashlib.md5())
    print(hash_str)


def test_file_hash_generator():
    dir_path = Path("/home/chad/projects/utilities/tests/utilities")
    file_path_list = dir_path.glob("**/*.py")
    f_gen = get_file_hash_generator(file_path_list, hashlib.md5())
    for x in f_gen:
        print(x)


def test_file_hash_generator2():
    dir_path = Path("/home/chad/projects/")
    file_path_list = dir_path.glob("**/*")
    f_gen = get_file_hash_generator(file_path_list, hashlib.md5())
    for count, x in enumerate(f_gen):
        pass
    print(f"Files: {count+1}")
