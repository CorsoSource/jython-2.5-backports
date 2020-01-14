from __future__ import absolute_import
# Copyright (c) 2010-2019 openpyxl

# from openpyxl.compat import unicode

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.descriptors.base import (
    # Sequence,
    Alias
)
from openpyxl.descriptors.sequence import Sequence


class AuthorList(Serialisable):

    tagname = "authors"

    author = Sequence(expected_type=unicode)
    authors = Alias("author")

    def __init__(self,
                 author=(),
                ):
        self.author = author
