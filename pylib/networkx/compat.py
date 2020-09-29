from __builtin__ import property

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


try:
    next
except NameError:
    _sentinel = object()
    def next(it, default=_sentinel):
        try:
            return it.next()
        except StopIteration:
            if default is _sentinel:
                raise
            return default
else:
    locals()['next'] = next


def isnan(x):
    """https://stackoverflow.com/a/44154660/13229100"""
    return (x != x)


# https://docs.python.org/2/library/itertools.html#itertools.combinations

class ZipExhausted(Exception):
    pass

def izip_longest(*args, **kwds):
    # izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    fillvalue = kwds.get('fillvalue')
    counter = [len(args) - 1]
    def sentinel():
        if not counter[0]:
            raise ZipExhausted
        counter[0] -= 1
        yield fillvalue
    fillers = repeat(fillvalue)
    iterators = [chain(it, sentinel(), fillers) for it in args]
    try:
        while iterators:
            yield tuple(map(next, iterators))
    except ZipExhausted:
        pass

def product(*iterables):
    """ Equivalent of itertools.product for versions < 2.6,
        which does NOT build intermediate results.
        Omitted 'repeat' option.
        product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy

        https://stackoverflow.com/a/7450757/13229100
    """
    nIters = len(iterables)
    lstLenths = []
    lstRemaining = [1]
    for i in xrange(nIters-1,-1,-1):
        m = len(iterables[i])
        lstLenths.insert(0, m)
        lstRemaining.insert(0, m * lstRemaining[0])
    nProducts = lstRemaining.pop(0)

    for p in xrange(nProducts):
        lstVals = []

        for i in xrange(nIters):
            j = p/lstRemaining[i]%lstLenths[i]
            lstVals.append(iterables[i][j])
        yield tuple(lstVals)

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

# for completeness and easier refactoring
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

setattr(chain, 'from_iterable', from_iterable)
