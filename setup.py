from setuptools import setup

setup(
    name='PythonExtended',
    url='https://github.com/RobertJN64/PythonExtended',
    author='Robert Nies',
    author_email='robertjnies@gamil.com',
    # Needed to actually package something
    packages=['PythonExtended'],
    # Needed for dependencies
    #install_requires=['pygame'],
    # *strongly* suggested for sharing
    version='0.0.1',
    # The license can be anything you like
    license='MIT',
    description='A collection of libraries that run on top of existing python libraries. Used to make function easier. Focus on object oriented and functional programming',
    long_description=open('README.txt').read(),
    #data_files=[('tests', ['tests/test.py']),
               # ('tests/files', ['tests/files/titanic.json'])],
)