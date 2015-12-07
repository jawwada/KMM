# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:49:25 2015
@author: ahmed
"""
import os
os.chdir("/sandbox/KMM")

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import street_network as sn
from shapely.geometry import LineString,Point

#reading the files and parsing the linestring

network   = sn.RoadNetwork()
gps_p     = sn.GPSPoints()

network.parse_streets()

utils = sn.MMUtils(gps_p,network)
#utils.find_closest_routes(100)

streets = network.streets
gps     = gps_p.gps

'''
Tesing Code
'''
print streets['LINESTRING'][1].replace('\'','')

line=LineString(streets['LINESTRING'][1])


'''
plt.figure()
streets['points'].map(lambda x: plt.plot(x[1::2],x[0::2]))
plt.plot(gps.ix[:,2:4],'+')
plt.show()
#make a dict out of a dataframe
#streets_dict = dict(zip(streets['Edge ID'] ,streets['points'] ))
print gps.ix[:,2:4]
print streets['LINESTRING'].head()

Tesing Code Finished
'''
    