from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='AIVA-barcode-recognition',
    version='0.1.0',
    long_description=readme,
    author='Susana Pineda y Álvaro Gómez Haro',
    url='https://github.com/alvarogharo/AIVA-barcode-recognition',
    packages=find_packages(exclude=('tests', 'docs'))
)
