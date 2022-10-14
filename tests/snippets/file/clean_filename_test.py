####################################################
#                                                  #
#   tests/snippets/file/clean_filename_test.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-14T08:58:15-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from snippets.file.clean_filename import clean_filename_invalid, clean_filename_valid


def test_date_string_valid():
    test_string = "2022-10-14T15:47:24.976314+00:00"
    expected = "2022-10-14T15_47_24.976314_00_00"
    clean_string = clean_filename_valid(test_string)
    assert expected == clean_string


def test_date_string_invalid():
    test_string = "2022-10-14T15:47:24.976314+00:00"
    expected = "2022-10-14T15_47_24.976314+00_00"
    print(test_string)
    clean_string = clean_filename_invalid(test_string)
    assert ":" not in clean_string
    assert expected == clean_string
