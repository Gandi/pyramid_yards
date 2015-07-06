import re
import os
import sys
from setuptools import setup, find_packages

name = 'pyramid_yards'
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(here, 'CHANGES.rst')) as changes:
    CHANGES = changes.read()

with open(os.path.join(here,
                       name.replace('-', '_'),
                       '__init__.py')) as v_file:
    version = re.compile(r".*__version__ = '(.*?)'",
                         re.S).match(v_file.read()).group(1)

requires = ['pyramid',
            'colander>=1.0b1'
            ]

extras_require = {'dev': ['Babel']
                  }


setup(name=name,
      version=version,
      description='Pyramid Request Parameter Validation',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Intended Audience :: Developers",
          "License :: Repoze Public License",
        ],
      author='Guillaume Gauvrit',
      author_email='guillaume@gauvr.it',
      url='https://github.com/Gandi/pyramid_yards',
      keywords='pyramid colander',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pyramid_yards.tests',
      install_requires=requires,
      extras_require=extras_require,
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      )
