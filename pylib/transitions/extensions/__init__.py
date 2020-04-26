"""
transitions.extensions
----------------------

Additional functionality such as hierarchical (nested) machine support, Graphviz-based diagram creation
and threadsafe execution of machine methods. Additionally, combinations of all those features are possible
and made easier to access with a convenience factory.
"""

from transitions.extensions.diagrams import GraphMachine
from transitions.extensions.nesting import HierarchicalMachine
from transitions.extensions.locking import LockedMachine

from transitions.extensions.factory import MachineFactory, HierarchicalGraphMachine, LockedHierarchicalGraphMachine
from transitions.extensions.factory import LockedHierarchicalMachine, LockedGraphMachine
