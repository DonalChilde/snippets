####################################################
#                                                  #
#         src/snippets/file/line_count.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-12-03T12:11:37-07:00            #
# Last Modified: 2022-12-03T23:43:00.749902+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from pathlib import Path


def line_count(file_name: Path) -> int:
    total = 0
    with file_name.open(mode="rt", encoding="utf-8") as file_in:
        for count, _ in enumerate(file_in, start=1):
            total = count
    return total
