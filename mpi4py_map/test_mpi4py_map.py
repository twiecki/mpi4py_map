#!/bin/env python

import mpi4py_map


if __name__ == "__main__":
    print """Run this file with mpirun, e.g.:
    mpirun -n 4 test_mpi4py_map"""
    result = mpi4py_map.test_map()

