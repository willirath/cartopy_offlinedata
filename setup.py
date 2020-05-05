from setuptools import setup

setup(name='cartopy_offlinedata',
      version='0.2.3',
      description='Add shared data path to cartopy config',
      url='https://github.com/willirath/cartopy_offlinedata',
      author='Willi Rath',
      author_email='wrath@geomar.de',
      license='MIT',
      packages=['cartopy_userconfig'],
      scripts=['bin/download_cartopy_data.sh'],
      zip_safe=False)
