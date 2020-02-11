from setuptools import setup
import os
import re

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'cartopy_userconfig', '__init__.py')) as f:
    init_file = f.read()

version = re.search(r'{}\s*=\s*[(]([^)]*)[)]'.format('__version_info__'),
                    init_file).group(1).replace(', ', '.')

setup(name='cartopy_offlinedata',
      version=version,
      description='Add shared data path to cartopy config',
      url='https://git.geomar.de/open-source/cartopy_offlinedata',
      author='Willi Rath',
      author_email='wrath@geomar.de',
      license='MIT',
      packages=['cartopy_userconfig'],
      scripts=['bin/download_cartopy_data.sh'],
      zip_safe=False)
