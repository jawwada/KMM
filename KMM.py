
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



utils = sn.MMUtils(gps_p,nw)
#utils.find_closest_routes(100)

streets = nw.streets
gps     = gps_p.gps


closest=[k for k in nw.network_dict for y in gps_p.points_list \
            if y.distance(nw.network_dict[k]) < 1000]

cl=streets[streets["Edge ID"].isin(closest)]
plt.figure()

for index, i in cl.iterrows():
    plt.plot(i['Long'],i['Lat'])
plt.show()


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
    

'''
'''
Tesing Code Finished    
'''