from setuptools import setup
from Cython.Build import cythonize

setup(
    name='TechQA tools',
    ext_modules=cythonize("src/techqa_tools/techqa_tools.pyx"),
)
