# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:10:26 2020

@author: TimK
"""

import pandas as pd
import datetime

# separate closest station and distance 
a = ['a', 'b', 'c', 'd']
print(''.join(a))


import pgeocode # credit Authors: Roman Yurchak <roman.yurchak@symerio.com>

dist = pgeocode.GeoDistance('GB')
# dist.query_postal_code('RM18', 'W2 2SZ')


df = pd.read_csv('C:/Users/TimK/Documents/ds_zoop_proj/zoopla.csv')

# convert price to number
df = df[df['price']!= 'POA']
df['price'] = df['price'].apply(lambda x: int(x.split()[0].replace(',', '')))

# separate closest station and distance 
closest_st = df['closest_station'].apply(lambda x: x.split('(')[0].strip())
closest_st_miles = df['closest_station'].apply(lambda x: float(x.split('(')[-1].split(' ')[0]))
postcode = df['address'].apply(lambda x: str(x.split()[-1]))
df['closest_station'] = closest_st
df['closest_st_miles'] = closest_st_miles
df['prop_pc'] = postcode
# add a series which shows the distance in miles from postcode to central london (W2 2SZ)  
d_from_c = postcode.apply(lambda x:(dist.query_postal_code(x,'W2 2SZ')/1.6))
df['d_from_c'] = d_from_c

# convert listed to data
df['listed_on_2'] = df['listed_on'].apply(lambda x: x.split("'on',")[-1].strip("]").replace("',","").replace("'",""))
# df['listed_on_2'] = df['listed_on_2'].apply(lambda x: ''.join(x))
# remove unnamed column

df.to_csv('zoopla_data_cleaned.csv')