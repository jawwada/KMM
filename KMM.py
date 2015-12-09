
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
import shapelytools as st
import pyproj
#reading the files and parsing the linestring
gps_points=100
dist_thresh=100

nw   = sn.RoadNetwork()
gps_p     = sn.GPSPoints()

utils = sn.MMUtils(gps_p,nw)
#utils.find_closest_routes(100)

streets = nw.streets
gps     = gps_p.gps


closest=[k for k in nw.network_dict for y in gps_p.points_list[1:gps_points] \
        if y.distance(nw.network_dict[k]) < dist_thresh]

cl=streets[streets["Edge ID"].isin(closest)]

small_nw = {key: nw.network_dict[key] for key in cl["Edge ID"]}

closest_nw = dict()

for i in range(len(gps_p.points_list[1:gps_points])):
    closest_nw[i] = tuple(reversed(min((gps_p.points_list[i].distance(geom), k) \
                    for k, geom in small_nw.iteritems())))

point_edge_dict={k:v[0] for k,v in closest_nw.iteritems()}

print point_edge_dict

nearest_points = [st.project_point_to_object(gps_p.points_list[p],small_nw[e])
                 for p,e in point_edge_dict.iteritems()]

long_proj = [x.coords.xy[0][0] for x in nearest_points]
lat_proj  = [x.coords.xy[1][0] for x in nearest_points]
proj = pyproj.Proj("+proj=utm +zone=10T, +north +ellps=WGS84 +datum=WGS84 +units=m")
xx, yy = proj(long_proj, lat_proj, inverse=True)

plt.figure()
#project_point_to_object(point, geometry)
#closest_object(geometries, point):
for index, i in cl.iterrows():
    plt.plot(i['Long'],i['Lat'])

plt.plot(xx,yy,'ro')
plt.plot(gps.ix[1:gps_points,"Longitude"],gps.ix[1:gps_points,"Latitude"],'b.')
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
