import codecs
import re
import os
import pathlib

from setuptools import find_packages, setup


def get_version(filename):
    with codecs.open(filename, 'r', 'utf-8') as fp:
        contents = fp.read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", contents).group(1)


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
NAME = 'py_serpro_biodata'
VERSION = get_version(os.path.join('py_serpro_biodata', '__init__.py'))
DESCRIPTION = 'Python lib não oficial do serviço BIOValid do SERPRO no Brasil'
URL = 'https://github.com/juliosmelo/py_serpro_biodata'
AUTHOR = 'Julio Melo'
AUTHOR_EMAIL = 'juliocsmelo@gmail.com'
LICENSE = 'MIT'
PACKAGES = ['py_serpro_biodata']
REQUIREMENTS = ['requests', 'cryptography', 'python-jose']
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: Portuguese',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: System :: Installation/Setup']

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description_content_type='text/markdown',
      long_description=README,
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      packages=find_packages(exclude=("py_serpro_biodata/tests",)),
      install_requires=REQUIREMENTS,
      include_package_data=True,
      classifiers=CLASSIFIERS,
      zip_safe=False)
