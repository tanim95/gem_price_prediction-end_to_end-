from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [i.replace('\n', '') for i in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name='gem_price_prediction',
    version='0.0.1',
    author='tanim',
    author_email='tanimrahman78@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
