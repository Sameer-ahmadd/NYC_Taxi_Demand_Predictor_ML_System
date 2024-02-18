from setuptools import setup, find_packages

setup(
    name='src',
    version='1.0',
    author='Your Name',
    author_email='your@email.com',
    description='Your package description',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],  # add any dependencies here
)
