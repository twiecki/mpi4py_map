
from distutils.core import setup

setup(
    name="mpi4py_map",
    version="0.2",
    author="Thomas V. Wiecki",
    author_email="thomas.wiecki@gmail.com",
    url="http://github.com/twiecki/mpi4py_map",
    description="mpi4py_map provides a simple map() interface to mpi4py that allows easy parallelization of function evaluations over sequential input.",
    install_requires=['mpi4py'],
    setup_requires=['mpi4py'],
    classifiers=[
                'Development Status :: 3 - Alpha',
                'Environment :: Console',
                'Operating System :: OS Independent',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering',
                 ]
)
