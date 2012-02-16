#!/bin/env python
import mpi4py_map

def power(x, y=2):
    return x**y


def test_power():
    result_parallel = mpi4py_map.map(power, range(50), y=2, debug=True)
    result_serial = [power(i, y=2) for i in range(50)]
    assert result_serial == result_parallel, "Parallel result does not match direct one."



if __name__ == "__main__":
    print """Run this file with mpirun, e.g.:
    mpirun -n 4 test_mpi4py_map"""

    test_power()

