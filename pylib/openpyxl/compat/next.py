

_sentinel = object()
def next(it, default=_sentinel):
    try:
        return it.next()
    except StopIteration:
        if default is _sentinel:
            raise
        return default
