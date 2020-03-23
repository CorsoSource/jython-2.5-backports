# jython-2.5-backports
Backported libraries for use in Ignition's Jython 2.5 environment

To use simply copy the contents of the `pylib` folder to your Ignition's installation under `./user-lib./pylib`. 
For example, by default this will be
`C:\Program Files\Inductive Automation\Ignition\user-lib\pylib`

# Process for backporting

Jython 2.5 is similar to - but not _quite_ - Python 2.5. For example, there is no [GIL](https://wiki.python.org/moin/GlobalInterpreterLock) and it has Unicode support. It also has some mechanical differences with Python 2.7, subtle things like different exception handling syntax, different underlying types, and missing/incomplete builtins (many added in Python 2.6). 

When a core library from Python 2.7 is needed but not implemented in Jython 2.5, we can often directly reimplement the functionality from [PyPy](https://www.pypy.org/). The source code provides a full (and often performant!) implementation of Python in Python itself! That means that just about any function can be ported and made to work into Jython. Usually I search in the `[pypy]./lib-python/2.7/`.

A few techniques are used:
 - Find/replace to enumerate the code that needs changing.
 - Libraries backported from Python 2.7 via PyPy.
 - Monkey patching incorrect or incomplete functions.
 - Rename, redirect, and wrap incompatible functions.

# Contributors

Please submit a pull request or open an issue for direction on something to add! 
