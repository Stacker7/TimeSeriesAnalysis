from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path : str) -> List[str] :
    """
    Function to return the list of requirements for this program.
    """
    requirements = []
    with open(file_path, 'r') as req_file:
        requirements = req_file.readlines()
        if '-e .' in requirements :
            requirements.remove('-e .')
    return requirements

setup(
    name = 'TIMESERIESANALYSIS',
    version = '0.0.1',
    author = 'Stacker7',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)