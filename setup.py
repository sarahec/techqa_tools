from setuptools import setup
from Cython.Build import cythonize

install_requires=[
   'jsonlines',
    'spacy',
]

setup(
    name='TechQA tools',
    ext_modules=cythonize("src/techqa_tools/tools.py"),
)
