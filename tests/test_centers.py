#!/usr/bin/env python

# Read in the map.yml file to validate each entry. Specifically:
# A name, url, and coord is required.
# optional fields are institution, image

import pytest
import requests
import yaml
import os
import re

def test_map():

    here = os.path.dirname(os.path.abspath(__file__))
    centers_file = os.path.join(os.path.dirname(here), '_data', 'centers.yml')       
    print("Testing loading of the centers.yml file")
    assert os.path.exists(centers_file)
    with open(centers_file, 'r') as stream:
        mapdata = yaml.safe_load(stream)

    print("validate required fields are provided")
    requireds = ['name', 'coords', 'external_url', 'id', 'resource_name']
    UA="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"

    # Also make sure ids are unique
    uids = set()
    for entry in mapdata:

        print("Testing %s" % entry)
        for required in requireds:
            print('Looking for %s' % required)
            assert required in entry

        print("Testing for lowercase letters in %s" % entry['id'])
        for c in entry['id']:
            if c != "-" and c not in [str(x) for x in range(0,9)]:
                assert c.islower() is True
 
        # Don't allow (403 response)
        skips = "(uni[.]lu|leeds|kb[.]iu|army|ethz)"

        # Test that url is 200
        if not re.search(skips, entry['external_url']):
            response = requests.head(entry['external_url'])
            assert response.status_code in [200, 300, 301, 302]
 
        # Image must exist
        if 'image' in entry:
            response = requests.get(entry['image'], headers={"User-Agent": UA})
            assert response.status_code == 200

        # Coords must be length 2, and int
        assert len(entry['coords']) == 2
        for coord in entry['coords']:
            assert isinstance(coord, float)

        # We cannot have the uid
        assert entry['id'] not in uids
        uids.add(entry['id'])
