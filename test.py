#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pyIndego import IndegoClient
from svgutils.transform import fromfile, fromstring
from os.path import exists

def main(config):
    with IndegoClient(**config) as indego:

        print(f'Updating mower state...')
        indego.update_state()

        print(f'{indego.state}')

if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    main(config)
