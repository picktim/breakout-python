import glob
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

ext_modules = [
    Pybind11Extension('breakout', sorted(glob.glob('breakout/*.cpp')))
]

setup(
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext}
)
