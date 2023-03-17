####################################################
#                                                  #
#      src/snippets/file/dicts_to_csv.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-13T11:41:58-07:00            #
# Last Modified: 2023-03-17T21:23:38.160492+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

import csv
from pathlib import Path
from typing import Dict, Iterable

from snippets.file.validate_file_out import validate_file_out


def dicts_to_csv(
    dicts: Iterable[Dict],
    output_path: Path,
    *,
    overwrite_ok: bool = False,
    write_header: bool = True,
    **kwargs,
):
    """
    Save an iterable of dicts to csv.

    The file output path will be checked for validity. Existing files will not be
    overwritten unless overwrite_ok = True. Invalid file paths will throw a ValueError.
    Parent directories will be created as necessary.

    Args:
        dicts: the dicts to save.
        output_path: The file path to the csv.
        overwrite_ok: Overwrite an existing file. Defaults to False.
        write_header: Write the first line as field headers. Defaults to True.

    Raises:
        ValueError: Raised for invalid file paths, or no dicst to save.
    """
    validate_file_out(output_path, overwrite=overwrite_ok, ensure_parent=True)
    iter_dict = iter(dicts)
    try:
        first = next(iter_dict)
    except StopIteration as exc:
        raise ValueError("No data available to save as csv.") from exc
    fieldnames = kwargs.pop("fieldnames", [])
    if not fieldnames:
        fieldnames = list(first.keys())
    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, **kwargs)
        if write_header:
            writer.writeheader()
        writer.writerow(first)
        writer.writerows(iter_dict)
