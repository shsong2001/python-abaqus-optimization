# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:52:24 2016

@author: Jens
"""

import json

def dump_data (data, name):
    "Dump to json file"
    f = open(name, 'w')
    f.truncate()
    json.dump(data, f, sort_keys=True)
    f.close()
    
def load_data(name):
    "Load json file"
    f = open(name, 'r')
    out = json.load(f)
    f.close()
    return out

