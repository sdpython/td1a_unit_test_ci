# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

here = os.path.dirname(__file__)
packages = find_packages(where=here)
package_dir = {k: os.path.join(here, k.replace(".", "/")) for k in packages}


setup(name='td1a_unit_test_ci',
      version='0.1',
      description="module très simple pour essayer l'inégration continue",
      author='Xavier Dupré',
      author_email='xavier.dupre@gmail.com',
      url='https://github.com/sdpython/td1a_unit_test_ci',
      packages=packages,
      package_dir=package_dir)
