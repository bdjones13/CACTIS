.. CycleGraph:

==========
CycleGraph
==========


.. currentmodule:: cactis

``CycleGraph`` is for building directed, unweighted cycle graphs. It is a class built on top of our ``Digraph`` class. Within the ``Digraph`` class, it is possible to add weights to these cycle graphs. 

Usage::

   cycle_graph = CycleGraph(n)

``n`` is the number of vertices in the desired cycle graph.


.. autoclass:: CycleGraph
   :members: __init__