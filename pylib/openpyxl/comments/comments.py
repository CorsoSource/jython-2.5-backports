from __future__ import absolute_import
# Copyright (c) 2010-2019 openpyxl


try:
    _ = property.setter
except AttributeError:
    #https://stackoverflow.com/a/25483289
    import __builtin__
    class _property(__builtin__.property):
        def getter(self, fget):
            return __builtin__.property(fget, self.fset, self.fdel)
        def setter(self, fset):
            return __builtin__.property(self.fget, fset, self.fdel)
        def deleter(self, fdel):
            return __builtin__.property(self.fget, self.fset, fdel)
    property = _property


class Comment(object):

    _parent = None

    def __init__(self, text, author, height=79, width=144):
        self.content = text
        self.author = author
        self.height = height
        self.width = width


    @property
    def parent(self):
        return self._parent


    def __eq__(self, other):
        return (
            self.content == other.content
            and self.author == other.author
        )

    def __repr__(self):
        return "Comment: %s by %s" % (self.content, self.author)


    def __copy__(self):
        """Create a detached copy of this comment."""
        clone = self.__class__(self.content, self.author, self.height, self.width)
        return clone


    def bind(self, cell):
        """
        Bind comment to a particular cell
        """
        if cell is not None and self._parent is not None and self._parent != cell:
            fmt = "Comment already assigned to %s in worksheet %s. Cannot assign a comment to more than one cell"
            raise AttributeError(fmt % (cell.coordinate, cell.parent.title))
        self._parent = cell


    def unbind(self):
        """
        Unbind a comment from a cell
        """
        self._parent = None


    @property
    def text(self):
        """
        Any comment text stripped of all formatting.
        """
        return self.content

    @text.setter
    def text(self, value):
        self.content = value
