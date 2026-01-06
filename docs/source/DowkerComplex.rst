.. DowkerComplex:

=============
DowkerComplex
=============

This construction of the Dowker complex builds a Gudhi ``SimplexTree`` object based on a potentially asymmetric distance matrix and is taken directly from Niklas Hellmer and Jan Spalinski's pyDowker, https://github.com/nihell/pyDowker. The DowkerComplex can then be fed into Gudhi's persistent homology algorithm. 

Usage::

   complex = DowkerComplex(D)

``D`` is the distance matrix, or more generally, the relation used to build the Dowker complex. In our case, this will be the distance matrix for the directed graph formed by binning the dynamical system.

.. currentmodule:: cactis

.. autoclass:: DowkerComplex
   :members: __init__