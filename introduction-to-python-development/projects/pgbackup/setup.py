from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0'
    author='Connor Rhodes'
    author_email='connor@rhodes.contact'
    description='A utility for backing up PostgreSQL databases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://raw.githubusercontent.com/0xConnorRhodes/python-playground/main/introduction-to-python-scripting/projects/pgbackup',
    packages=find_packages('src')
)