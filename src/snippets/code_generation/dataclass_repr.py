####################################################
#                                                  #
#  src/snippets/code_generation/dataclass_repr.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-23T22:26:04-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from dataclasses import dataclass, fields


@dataclass
class Example:
    author: str
    book: str
    ident: str

    def __repr__(self):
        # from Fluent Python 2ed. p189
        cls = self.__class__
        cls_name = cls.__name__
        # dataclass version
        field_names = (field.name for field in fields(cls))
        # NamedTuple version
        # field_names = (field.name for field in self._fields)
        # Class version
        # field_names = (key for key in self.__dict__ if not key.startswith("_"))
        indent = " " * 4
        rep = [f"{cls_name}("]
        for field in field_names:
            value = getattr(self, field)
            rep.append(f"{indent}{field} = {value!r}")
        rep.append(")")
        return "\n".join(rep)
