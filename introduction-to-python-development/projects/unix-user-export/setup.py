from setuptools import find_packages, setup

with open('README.rst', encoding='UTF-8') as f:
    long_description = f.read()

setup(
    name='hr',
    version='0.1.0',
    author='Connor Rhodes',
    author_email='connor@rhodes.contact',
    description-'Utility to export user information on a unix system',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://raw.githubusercontent.com/0xConnorRhodes/python-playground/main/introduction-to-python-scripting/projects/unix-user-export',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
)
