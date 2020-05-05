#!/usr/bin/env python
import argparse
import os
import urllib.request
import tempfile
import cartopy
from cartopy import config
import sys


def main(target_dir):
    try:
        os.makedirs(target_dir)
    except OSError:
        pass

    version = cartopy.__version__

    with tempfile.TemporaryDirectory() as tmpdirname:
        target_dir = os.path.abspath(target_dir)
        owd = os.getcwd()
        os.chdir(tmpdirname)
        urllib.request.urlretrieve(
            'https://raw.githubusercontent.com/SciTools/cartopy/v{}/tools/feature_download.py'.format(version),
            'feature_download.py')

        file = open('__init__.py', 'w')
        file.close()

        sys.path.append(tmpdirname)

        from feature_download import FEATURE_DEFN_GROUPS, download_features

        # add Antarctic ice shelves
        FEATURE_DEFN_GROUPS['physical'] = \
            FEATURE_DEFN_GROUPS['physical'] + \
            (('physical', 'antarctic_ice_shelves_polys', ('50m', '10m')),)

        config['pre_existing_data_dir'] = target_dir
        config['data_dir'] = target_dir
        config['repo_data_dir'] = target_dir
        download_features(
            ['cultural-extra', 'cultural', 'gshhs', 'physical'], dry_run=False)
        os.chdir(owd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download cartopy data for caching.')
    parser.add_argument('--output', '-o', required=True,
                        help='save datasets in the specified directory')
    args = parser.parse_args()
    main(args.output)
