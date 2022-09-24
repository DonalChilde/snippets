"""[summary]

https://stackoverflow.com/a/3431835/105844

Returns:
    [type] -- [description]

Yields:
    [type] -- [description]
"""
import hashlib
from io import BufferedReader
from pathlib import Path
from typing import BinaryIO, ByteString, Iterator, Sequence, Union


def hash_a_byte_str_iterator(
    bytes_iter: Iterator[ByteString], hasher, as_hex_str: bool = False
):
    result = None
    for block in bytes_iter:
        # print(f"Block {block}")
        hasher.update(block)
        if as_hex_str:
            result = hasher.hexdigest()
        else:
            result = hasher.digest()
    return result


def file_as_block_iterator(
    file_handle: BinaryIO, blocksize: int = 65536
) -> Iterator[ByteString]:
    with file_handle:
        block = file_handle.read(blocksize)
        while len(block) > 0:
            # print(f"Block {block}")
            yield block
            block = file_handle.read(blocksize)


# def get_hasher(hasher_name: str):
#     lc_hasher_name = hasher_name.lower()
#     hasher_lookup = {"md5": hashlib.md5}
#     hasher = hasher_lookup.get(lc_hasher_name, None)
#     if hasher is None:
#         raise ValueError(f"Hasher {hasher_name} not found")
#     return hasher()


def get_file_hash(file_path: Path, hasher):

    file_hash_str = None
    with open(file_path, "rb") as file_handle:
        file_hash_str = hash_a_byte_str_iterator(
            file_as_block_iterator(file_handle), hasher=hasher, as_hex_str=True
        )
    return file_hash_str


def get_file_hash_generator(file_paths: Sequence[Path], hasher):
    # hash_method = get_hasher(hash_method_name)
    generator = (
        (file_path, get_file_hash(file_path, hasher))
        for file_path in file_paths
        if file_path.is_file()
    )
    return generator
