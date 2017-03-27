# -*- coding:utf-8 -*- 
'''Override cartopy.config to be able to include offline data.'''

import os
import logging

def update_config(config):
    '''Set cartopy's pre_existing_data_dir to $CARTOPY_OFFLINE_SHARED.'''

    try:
        config['pre_existing_data_dir'] = os.environ['CARTOPY_OFFLINE_SHARED']

        logging.warning('Setting cartopy.config["pre_existing_data_dir"] to {}.'
                ' Don\'t worry, this is probably intended behaviour to avoid'
                ' failing downloads of geological data behind a firewall.'
                ''.format(os.environ['CARTOPY_OFFLINE_SHARED']))
    except:
        pass


