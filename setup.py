from setuptools import setup
from pathlib import Path

setup(
    name='pyWRspice',
    version='0.1',
    author='Raytheon BBN Technologies - QEC Group',
    packages=["pyWRspice"],
    package_data={'pyWRspice':['data/*.csv','data/*.py']},
    scripts=[],
    url='https://github.com/BBN-Q/pyWRspice',
    license='MIT License',
    description='Python wrapper for WRspice circuit simulation',
    long_description=Path('README.md').read_text(encoding='utf-8'),
    python_requires='>=3.10',
    install_requires=[
        "numpy >= 2.0",
        "scipy >= 1.7.0",
        "pandas >= 2.0",
        "paramiko >= 2.9.5",
        "networkx",
        "matplotlib",
        "bbnadapt",
    ],
)
