####################################################
#                                                  #
# src/snippets/inspection/full_name.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-19T10:10:35-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################


def fullname(obj) -> str:
    if type(obj).__qualname__ != "type":
        # obj is instance
        return ".".join(
            [
                obj.__class__.__module__,
                obj.__class__.__qualname__,
            ]
        )
    # obj is not instance
    return ".".join([obj.__module__, obj.__qualname__])
