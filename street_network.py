# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:29:42 2015
@author: ahmed
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point,LineString
import pyproj


class GPSPoints:
    ''' Class for storing and parsing of GPS data
    '''
    gps = pd.DataFrame
    points_list = list
    
    def __init__(self,in_file="gps_data.txt"):
        
        self.read_gps_file(in_file)
        self.transform_and_append()
        
        self.points_list = [Point(x) for x in zip(self.gps["LongProj"].values,\
                            self.gps["LatProj"].values)]
        
    def read_gps_file(self,in_file):
        ''' Reads the GPS file into gps data frame of the class.
        '''
        try:
            self.gps = pd.read_csv(in_file, sep='\t')
        except:
            print "I/O Error"
        
        self.gps.pop('Unnamed: 4')
        self.gps.pop('Unnamed: 5')
        self.gps = self.gps.rename(columns=lambda x: x.replace(',', 't'))

    def transform_and_append(self):
        ''' Transform the coordinates to utm projections and append to data frame
            of gps in the class
         '''
        proj = pyproj.Proj("+proj=utm +zone=10T, +north +ellps=WGS84 +datum=WGS84 +units=m")
        xx, yy = proj(self.gps["Longitude"].values, self.gps["Latitude"].values)
        self.gps['LongProj'] =   xx
        self.gps['LatProj']  =   yy
        

class RoadNetwork:    
    '''class for storing and parsing Road network data
    '''
    streets = pd.DataFrame
    network_dict = dict
   
    def __init__(self,in_file="road_network.txt"):
        '''The constructor is called with the input file for street network
            as a parameter and it executes the functions needed to parse the 
            unput file in a data frame
        '''
        self.read_streets_file(in_file)
        self.parse_streets()
        self.transform_and_append()
        self.make_network_dict()
    
    def read_streets_file(self, in_file):
        ''' Reads the in_file and puts the results into streets data frame
        
        '''
        
        try:
            self.streets=pd.read_csv(in_file, sep='\t')
        except: 
            print "I/O Error"
        
    def make_network_dict(self):
        
        self.network_dict=dict(zip(self.streets["Edge ID"].values, \
                    [LineString(x) for x in self.streets['transform']]))
                    
    def transform_and_append(self):
        
        proj = pyproj.Proj("+proj=utm +zone=10T, +north +ellps=WGS84 +datum=WGS84 +units=m")
        streets=self.streets
        streets['transform'] = streets['LINESTRING'].map(lambda x: [proj(j,k) for j,k in x])
        self.streets=streets
            
    def parse_streets(self):
    #stripping the linestrings from streets

        streets=self.streets
        streets['LINESTRING()'] = streets['LINESTRING()']. \
                                        map(lambda x: str(x)[:-1])
        streets['LINESTRING()'] = streets['LINESTRING()']. \
                                        map(lambda x: str(x)[11:])
        streets['LINESTRING()'] = streets['LINESTRING()']. \
                                        map(lambda x: str(x).replace('\'',''))
        streets['LINESTRING()'] = streets['LINESTRING()']. \
                                        map(lambda x: str(x).replace(',',''))
        streets['points']       = streets['LINESTRING()']. \
                                        map(lambda x: str(x).split(' '))
                                        
        #one can take all lats and longs by flatmapping a list
        #lats_all  = [l for item in streets['lat'] for l in item]
        #longs_all = [l for item in streets['long'] for l in item]
        streets['LINESTRING'] = streets['points'].\
                                map(lambda x: zip([float(i) for i in x[0::2]],\
                                [float(i) for i in x[1::2]]))
        
        streets['Long']= streets['points'].map(lambda x: [float(i) for i in x[0::2]])
        streets['Lat'] = streets['points'].map(lambda x: [float(i) for i in x[1::2]])
        self.streets=streets

class MMUtils:
    ''' class for map matching utilities
    '''
    
    gp = GPSPoints
    road_network = RoadNetwork
    
    def __init__(self,gps,road_network):
        self.gp = gps
        self.road_network = road_network

'''    
    i=0
    def find_closest_routes(self,dist_threshold):
        for street in self.road_network.streets['LINESTRING']:
            for gps_point in self.gp.gps.ix[:,2:4]:
                poly_line=LineString(street)
                point=point(gps_point)
                print poly_line.distance(point)
                i+=1
                if i==100 :
                    break;
            
'''     
    