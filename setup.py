from setuptools import find_packages, setup

setup(
    name='blocks.contrib',
    namespace_packages=['blocks'],
    install_requires=['blocks'],
    packages=find_packages(exclude=['examples']),
    zip_safe=False)
