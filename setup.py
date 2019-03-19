from setuptools import setup, find_packages

setup(
    name='MarPy',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/misakithecute/MarPy',
    author='Marissa Rutherford',
    author_email='marissa.rutherford@gmail.com'
)
