# try:
#     # don't execute this in sublime text
#     import sublime
# except ImportError:
from distutils.core import setup

setup(
    name='rocks',
    version='1.0',
    description='Rocks AutoTests',
    author='Jones Ambrosi',
    author_email='jones@centrimobi.com.br',
    url='http://rocks.io/',
    test_suite='nose2.collector.collector',
    # packages=find_packages(),
    packages=['rocks'],
    # namespace_packages=['test']
)
