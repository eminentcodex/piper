from setuptools import setup, find_packages

setup(
    name='piper',
    version='1.0',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['termcolor'],
    entry_points='''
        [console_scripts]
        piper=piper.main:main
    ''',
)