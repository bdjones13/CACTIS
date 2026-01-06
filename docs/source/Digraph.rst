.. Digraph:

=======
Digraph
=======

.. currentmodule:: cactis

For the parent class, see `networkx.DiGraph <https://networkx.org/documentation/stable/reference/classes/digraph.html>`_. 

``Digraph`` creates a NetworkX ``Digraph`` and includes methods for generating a distance matrix, changing the edge weights and retrieving the edge weights.  

Usage::

   directed_graph = DiGraph(adjacency_martix, vertices, counts, loops: bool)

``adjancency_matrix`` is either a binary or weighted matrix encoding the adjancency of the directed graph. ``vertices`` is the list of vertices, which in our use case is the list of nonempty bin numbers. ``counts`` is a list that is the weights of each vertex, and ``loops`` is a Boolean determing whether or not to keep the self-loops when building the graph. This would be associated with the situation when the dynamical system stays in the same bin for conseccutive time steps. 

Methods::

   D = Digraph.distance_matrix(method)

This method returns the distance matrix of the graph, as needed for homology computations. There are currently two tested methods, ``unweighted_shortest_path`` and ``weighted_shortest_path``. A third method, ``probabilistic``, is implemented but mostly untested, and could be an avenue for future research, where the bins become the states of a discretized view of the dynamical system as a Markov chain. Currently, if the graph is not strongly path connected, unreachable pairs are assigned a value of 1000. 

:: 

   Digraph.weight_graph(weights, smallest, biggest)

The ``weight_graph`` method allows for custom or random weighting of a directed graph. ``weights`` should be a callable function, that takes ``smallest`` and ``biggest`` as inputs, and assigns each edge in the directed graph a weight based on that function. For example, several of our experiments use ``numpy.random.randint``. 

::
   
   Digraph.get_weights()

``get_weights`` returns a dictionary whose keys are the edges of the directed graph, with associated values the weights of the edges. 


.. autoclass:: Digraph
   :members: __init__, distance_matrix, get_weights, weight_graph