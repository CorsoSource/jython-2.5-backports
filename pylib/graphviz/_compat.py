# _compat.py - Python 2/3 compatibility

import os
import sys
import operator
import subprocess

try:
    PY2 = (sys.version_info.major == 2)
except AttributeError:
    PY2 = (sys.version_info[0] == 2)


if PY2:
    string_classes = (str, unicode)  # needed individually for sublassing
    text_type = unicode

    iteritems = operator.methodcaller('iteritems')

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

    def makedirs(name, mode=0777, exist_ok=False):
        try:
            os.makedirs(name, mode)
        except OSError:
            if not exist_ok or not os.path.isdir(name):
                raise

    def stderr_write_bytes(data, flush=False):
        """Write data str to sys.stderr (flush if requested)."""
        sys.stderr.write(data)
        if flush:
            sys.stderr.flush()

    class CalledProcessError(subprocess.CalledProcessError):

        def __init__(self, returncode, cmd, output=None, stderr=None):
            super(CalledProcessError, self).__init__(returncode, cmd, output)
            self.stderr = stderr

        @property
        def stdout(self):
            return self.output

        @stdout.setter
        def stdout(self, value):  # pragma: no cover
            self.output = value


else:
    string_classes = (str,)
    text_type = str

    def iteritems(d):
        return iter(d.items())

    def makedirs(name, mode=0777, exist_ok=False):  # allow os.makedirs mocking
        return os.makedirs(name, mode, exist_ok=exist_ok)

    def stderr_write_bytes(data, flush=False):
        """Encode data str and write to sys.stderr (flush if requested)."""
        encoding = sys.stderr.encoding or sys.getdefaultencoding()
        sys.stderr.write(data.decode(encoding))
        if flush:
            sys.stderr.flush()

    CalledProcessError = subprocess.CalledProcessError
