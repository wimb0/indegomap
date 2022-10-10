#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pyIndego import IndegoClient
from svgutils.transform import fromfile, fromstring
from os.path import exists

def main(config):
    with IndegoClient(**config) as indego:

        print(f'Updating mower state...')
        indego.update_state(force=True)

        mapupdate = indego.state.map_update_available
        mapname = 'indegobasemap.svg'

        file_exists = exists(mapname)
        if mapupdate or not file_exists:
            print(f'Map update available: {mapupdate}')
            indego.download_map(filename=mapname)

        svg = fromfile(mapname)
        xpos = indego.state.svg_xPos
        ypos = indego.state.svg_yPos
        print(f'Indego position (x,y): {xpos},{ypos}')
        circle = f'<circle cx="{xpos}" cy="{ypos}" r="15" fill="yellow" />'
        mower_circle = fromstring(circle)

        print(f'Adding mower to map and save new svg...')
        svg.append(mower_circle)
        svg.save("updatedmap.svg")

if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    main(config)
