####################################################
#                                                  #
# src/snippets/package_resources/resource_line_reader.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-30T10:21:25-07:00            #
# Last Modified: 2023-04-30T18:48:33.630420+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

from importlib import resources
from typing import Iterable


def resource_line_reader(resource_package: str, resource_name: str) -> Iterable[str]:
    """Read a package file line by line. Assumes a text file."""
    resource_file = resources.files(resource_package).joinpath(resource_name)
    with resource_file.open() as txt_file:
        for txt in txt_file:
            yield txt
