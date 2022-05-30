import json
import pandas as pd
import numpy as np
from geopy import distance

def getDists(loca, locb):
    lata, longa = loca
    latb, longb = locb
    yDist = distance.distance(loca, (latb, longa)).miles
    xDist = distance.distance(loca, (lata, longb)).miles
    return abs(yDist) + abs(xDist)

df = pd.read_csv('~/Documents/zipCodes.txt') #read data

print(df.head()) #show stuff


df = df[df['ZIP']//10000 == 9] #select only california zip codes

school = np.array([df[df['ZIP'] == 94010]['LAT'],
                   df[df['ZIP'] == 94010]['LONG']])
        

school = np.array([school[0][0], school[1][0]])
coords = df[['LAT', 'LONG']].to_numpy()

dists = np.array(list(map(
    lambda x: getDists(x, school), 
    coords)))

print(dists.shape)

dists = dict(zip(df['ZIP'].to_list(), dists))

#print(dists)

with open('distances.json', 'w') as f:
    json.dump(dists, f)

