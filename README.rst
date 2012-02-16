Provides a map() interface to mpi4py.

License: MIT

Copyright (c) 2012 Thomas Wiecki (thomas.wiecki[at]gmail.com)

About
*****

MPI (Message Passing Interface) is a library that allows processes running on different hosts to communicate and exchange information. It is ideally suited for parallel computations on a cluster. mpi4py provides a convenient python wrapper for this library. However, it still a pretty bare exposition of MPI functions which requires you to code most of the interprocess-communication by hand. Other parallel python libraries such as the multiprocessing package (which only allows process management on a single host) have more simple interfaces. For example, you can create a worker pool and use the map() function to easily parallelize evaluations of your function over a given sequence (e.g. pool.map(lambda x: x**2, range(500)) will square the list in parallel).

mpi4py_map brings this simple but powerful map() functionality to mpi4py. It takes care of assigning the jobs to the workers, queueing if all workers are busy and cleanly shutting down all workers after the job is complete.

Features
********

* Easy, transparent parallelization of your Python code on a PC or cluster.
* Sequential items do not have to be serializable.

Dependencies
************

* MPI (OpenMPI or MPICH2)
* mpi4py (http://mpi4py.scipy.org/)

Usage
*****

Create a python file (e.g. mpi_square.py):

::

    from mpi4py_map import map
    print map(lambda x, y: x**y, [1,2,3,4], 2) # square the sequence

Then call your program with mpirun, e.g.:

::

    mpi4run -n 4 mpi_square.py
