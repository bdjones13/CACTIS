.. Trajectory

============
Trajectory
============

The trajectory module is responsible for the binning process to convert a time series to a matrix representing the adjacencies of bins, used as the adjacency matrix of the driected graph. The ``Trajectory`` object stores a time series, and the methods are used to get the coordinates of the bins, compute the one dimensional bin sequence of the time series, and generate the adjacency matrix of the graph. 

Usage::

   traj_ts = Trajectory(ts)

This builds an object in the ``Trajectory`` class based on a 2D numpy array, allowing for use of the following methods. 

Methods::

   bins = traj_ts.set_bins(b)
   


``set_bins`` is responsible for partitioning Euclidean space into bins based on the minimum and maximum value of the time series in each dimension. ``b`` is the number of bins in each dimension. 

::

   binseq = traj_ts.bin_sequence()

``bin_sequence`` returns a 1D array that is the same length of the time series. Each entry in this array is the number of the bin the time series is in at the current step. The number is the base ten representation of the base ``b`` list of current bin in each dimension, where the order of the dimensions is the same order of the columns in the original time series.  

::

   A, vertices, counts = traj_ts.adjacency(prob = False)

This returns the adjacency matrix of the directed graph built on the bins. If the time series moves from bin :math:`i` to bin :math:`j`, then one is added to the :math:`(i,j)` entry of the matrix ``A``. Two other 1D arrays, the list of nonempty bins and how frequently the time series is in each of those, are also returned by this method. The default is to give the weighted adjancency matrix, but ``prob = True`` would yield the matrix as a Markov matrix. 

::
   
   coordinates = traj_ts.bin_centers()

The ``bin_centers`` method contributes to the visualization of the directed graphs by locating and returning the center of each bin. 


.. currentmodule:: cactis

.. autoclass:: Trajectory
   :members: __init__, set_bins, bin_sequence, adjacency, bin_centers, ts