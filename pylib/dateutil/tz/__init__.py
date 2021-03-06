# -*- coding: utf-8 -*-
from dateutil.tz.tz import *
from dateutil.tz.tz import __doc__

#: Convenience constant providing a :class:`tzutc()` instance
#:
#: .. versionadded:: 2.7.0
UTC = tzutc()

__all__ = ["tzutc", "tzoffset", "tzlocal", "tzfile", "tzrange",
           "tzstr", "tzical", "tzwin", "tzwinlocal", "gettz",
           "enfold", "datetime_ambiguous", "datetime_exists",
           "resolve_imaginary", "UTC", "DeprecatedTzFormatWarning"]


class DeprecatedTzFormatWarning(Warning):
    """Warning raised when time zones are parsed from deprecated formats."""
