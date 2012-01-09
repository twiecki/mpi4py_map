#!/bin/env python

from mpi4py_map import map_async

def _power(x, y=2):
    return x**y

def test_map_async():
    import numpy as np
    result_parallel = map_async(_power, range(50), args=(2,), debug=True)
    result_serial = map(_power, range(50))
    assert np.all(result_serial == sorted(result_parallel)), "Parallel result does not match direct one."
    return sorted(result_parallel)

if __name__ == "__main__":
    print """Run this file with mpirun, e.g.:
    mpirun -n 4 test_mpi4py_map"""
    result = test_map_async()
    print result
