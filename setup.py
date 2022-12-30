#!python
#cython: language_level=3

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("main",  ["src/main.py"]),
    Extension("autoclick",  ["src/autoclick.py"]),
    Extension("autoloot",  ["src/autoloot.py"]),
    Extension("comon",  ["src/comon.py"]),
    Extension("pins",  ["src/pins.py"]),
    Extension("unbox",  ["src/unbox.py"]),
    Extension("utils",  ["src/utils.py"]),
    Extension("wood",  ["src/wood.py"]),
]

setup(
    name = 'scumHelper',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)