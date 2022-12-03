####################################################
#                                                  #
# src/snippets/pdf/extract_text_from_pdf_to_file.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-11-10T08:32:51-07:00            #
# Last Modified: 2022-12-03T23:48:13.872890+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

# Requires pdfminer.six

from pathlib import Path

from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

from snippets.file.validate_file_out import validate_file_out


def extract_text_from_pdf_to_file(
    file_in: Path,
    file_out: Path,
    overwrite: bool = False,
    la_params: LAParams | None = None,
):
    validate_file_out(file_path=file_out, overwrite=overwrite)
    with (
        open(file_out, mode="w", encoding="utf-8") as fp_out,
        open(file_in, mode="rb") as fp_in,
    ):
        if la_params is None:
            la_params = LAParams()
        extract_text_to_fp(fp_in, fp_out, laparams=la_params)
