
# Set default logging handler to avoid "No handler found" warnings.
# from logging import NullHandler
import logging
class NullHandler(logging.Handler):
    """
    This handler does nothing. It's intended to be used to avoid the
    "No handlers could be found for logger XXX" one-off warning. This is
    important for library code, which may contain code to log events. If a user
    of the library does not configure logging, the one-off warning might be
    produced; to avoid this, the library developer simply needs to instantiate
    a NullHandler and add it to the top-level logger of the library module or
    package.
    """
    def handle(self, record):
        pass

    def emit(self, record):
        pass

    def createLock(self):
        self.lock = None

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