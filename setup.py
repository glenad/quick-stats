from setuptools import setup, find_packages

setup(
    name='quickstats',
    version='0.1.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Common statistics utility functions',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'scipy'],
    url='https://github.com/glenad/quick-stats.git',
    author='Glen Adams',
    author_email='glen.adams@gmail.com'
)