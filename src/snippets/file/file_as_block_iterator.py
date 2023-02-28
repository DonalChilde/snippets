####################################################
#                                                  #
#   src/snippets/file/file_as_block_iterator.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-02-28T08:25:47-07:00            #
# Last Modified: 2023-02-28T15:35:03.278937+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################


from typing import BinaryIO, Iterator


def file_as_block_iterator(
    file_handle: BinaryIO, block_size: int = 2**10 * 64
) -> Iterator[bytes]:
    """
    Make an iterator for a file opened in binary mode.

    https://stackoverflow.com/a/3431835/105844
    https://www.pythonmorsels.com/reading-binary-files-in-python/

    Args:
        file_handle: The handle for file opened in binary mode.
        block_size: The size of the block to read. Defaults to 2**10*64 (64K).

    Yields:
        A block of bytes read from the file.
    """
    with file_handle:
        block = file_handle.read(block_size)
        while block:
            yield block
            block = file_handle.read(block_size)
