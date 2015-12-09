
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:49:25 2015
@author: ahmed
"""
from __future__ import division

import os
os.chdir("/sandbox/KMM")

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import street_network as sn
from   shapely.geometry import LineString , Point
import geopandas as gp
import itertools

#reading the files and parsing the linestring

nw   = sn.RoadNetwork()
gps_p     = sn.GPSPoints()



utils = sn.MMUtils(gps_p,network)
#utils.find_closest_routes(100)

streets = nw.streets
gps     = gps_p.gps




'''
    Tesing Code
    
#columnwise sum
# get the data types for all columns
print zip(gps.columns, [type(x) for x in gps.ix[0,:]])
print zip(streets.columns, [type(x) for x in streets.ix[0,:]])
#indexing in pandas

#order by speed limit

#group by speed limit
print streets.groupby(['Two Way']).count()
streets=pd.DataFrame(streets)
list(streets)
streets.boxplot(column=" Speed (m/s)", by="Two Way")
streets=streets.sort([" Speed (m/s)",'Two Way'])
#time series

#list comprehesnions

#implementing map, flatmap, filter, fold and reduce in python



#print streets['LINESTRING'][1].replace('\'','')
g_lat  = gp.GeoSeries(gps.ix[:,'Latitude'])
g_long = gp.GeoSeries(gps.ix[:,"Longitude"])
    
g_lat.plot()

line=LineString(streets['LINESTRING'][1])
print line
line.distance(Point(gps.ix[1,2:4]))
plt.figure()
streets['points'].map(lambda x: plt.plot(x[1::2],x[0::2]))
plt.plot(gps.ix[:,2:4],'+')
plt.show()
#make a dict out of a dataframe
#streets_dict = dict(zip(streets['Edge ID'] ,streets['points'] ))
print gps.ix[:,2:4]
print streets['LINESTRING'].head()

'''
'''
Tesing Code Finished    
'''