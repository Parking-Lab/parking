import json
import pandas as pd
import numpy as np


df = pd.read_csv('~/Documents/zipCodes.txt') #read data

print(df.head()) #show stuff


df = df[df['ZIP']//10000 == 9] #select only california zip codes

school = np.array([df[df['ZIP'] == 94010]['LAT'],
                   df[df['ZIP'] == 94010]['LONG']])
        

school = np.array([school[0][0], school[1][0]])
coords = df[['LAT', 'LONG']].to_numpy()

dists = coords-school
dist_abs = np.absolute(dists)
print(np.array(list(map(np.sum, dist_abs))))

dists = dict(
            zip
            (
                df['ZIP'].to_list(), 

                np.array
                (
                    list
                    (
                        map
                        (
                            np.sum, 
                            dist_abs
                        )
                    )
                )
            )
        )

print(dists)

with open('distances.json', 'w') as f:
    json.dump(dists, f)