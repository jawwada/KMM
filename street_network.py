# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:29:42 2015

@author: ahmed
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import point,LineString


class GPSPoints:
    gps = pd.DataFrame
    
    def __init__(self,in_file="/sandbox/KMM/gps_data.txt"):
        self.read_gps_file(in_file)
        
    def read_gps_file(self,in_file):
        self.gps = pd.read_csv(in_file, sep='\t')


class RoadNetwork:    
        
    streets = pd.DataFrame
    
    def __init__(self,in_file="/sandbox/KMM//road_network.txt"):
        self.read_streets_file(in_file)
        
    
    def read_streets_file(self, in_file):
        self.streets=pd.read_csv(in_file, sep='\t')
        
    
    def parse_streets(self):
    #stripping the linestrings from 
        streets=self.streets
        streets['LINESTRING()'] = streets['LINESTRING()'].map(lambda x: str(x)[:-1])
        streets['LINESTRING()'] = streets['LINESTRING()'].map(lambda x: str(x)[11:])
        streets['LINESTRING()'] = streets['LINESTRING()'].map(lambda x: str(x).\
                                  replace('\'',''))
        
        streets['LINESTRING()'] = streets['LINESTRING()'].map(lambda x: str(x).\
                                  replace(',',''))
        
        streets['points'] = streets['LINESTRING()'].map(lambda x: str(x).split(' '))
        streets['long']   = streets['points'].map(lambda x: x[0::2])
        streets['lat']    = streets['points'].map(lambda x: x[1::2])
        
        
        #one can take all lats and longs by flatmapping a list
        #lats_all  = [l for item in streets['lat'] for l in item]
        #longs_all = [l for item in streets['long'] for l in item]
        streets['LINESTRING'] = streets['points'].map(lambda x: zip(x[1::2],x[0::2]))
        self.streets=streets
        

class MMUtils:
    gp = GPSPoints
    road_network = RoadNetwork
    
    def __init__(self,gps,road_network):
        self.gp = gps
        self.road_network = road_network
    
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
            
            
        
    