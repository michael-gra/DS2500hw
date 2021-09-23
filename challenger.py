"""
Grace Michael
DS2500: Programming with Data
HW 2
"""

import csv
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

# This code is contributed by ChitraNayal (15-29) (geeksforgeeks link from class)
def haversine(lat1, lon1, lat2, lon2):
    # Python 3 program for the haversine formula distance between latitudes and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    # apply formula
    a = (pow(math.sin(dLat / 2), 2) + pow(math.sin(dLon / 2), 2) * math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c

# Stations Data
names = ['station_id', 'wban_id', 'lat', 'long']
stationsdf = pd.read_csv('stations.csv', names = names)
stationsdf = stationsdf.drop(columns=['wban_id'])
stationsdf = stationsdf.dropna()
stationsdf = stationsdf[(stationsdf.lat != 0.0) & (stationsdf.long != 0.0)]

# Calculate Haversine Distance
stationsdf['distance'] = stationsdf.apply(lambda row:haversine(row['lat'], row['long'], 28.396837, -80.605659), axis=1)
stationsdf.sort_values(by='distance', inplace = True)

# Keep within 100km closest to Cape Canaveral
near_stations = stationsdf[stationsdf.distance <=100]
near_stations = near_stations.drop_duplicates(subset=['station_id'])

# Temperatures Data
names2 = ['station_id', 'wban_id', 'month', 'day', 'temp']
tempdf = pd.read_csv('temp_1986.csv', names = names2)
tempdf = tempdf.drop(columns=['wban_id'])
tempdf = tempdf.dropna()

# January 28th
jan_28 = tempdf[(tempdf.month == 1) & (tempdf.day ==28)]

# January 28th near C.C.
totaldf = pd.merge(near_stations, jan_28)


# Estimate Cape Canaveral Temperature

estimate = (totaldf.temp/totaldf.distance).sum()/(1/totaldf.distance).sum()
temp_estimate = round(estimate, 2)

print('Estimated Temp at Cape Canaveral on Jan 28:', temp_estimate, 'degrees')

# Plot Cape Canaveral Temperature's January

january_df = tempdf[tempdf.month == 1]
cc_jan_df = pd.merge(near_stations,january_df)
cc_jan_df = cc_jan_df.sort_values(by=['day'])
cc_jan_df = cc_jan_df.drop(columns=['station_id', 'lat', 'long'])
cc_jan_df['weight'] = (cc_jan_df.temp/cc_jan_df.distance)
cc_jan_df['invs_dist'] = (1/cc_jan_df.distance)
cc_jan_df = cc_jan_df.groupby('day').sum()
cc_jan_df['estimate_temp'] = cc_jan_df['weight'] / cc_jan_df['invs_dist']

plt.plot(cc_jan_df.index.tolist(), cc_jan_df['estimate_temp'].tolist(), color='#000080',  marker = 'o')
plt.title("Cape Canaveral Temperature: January 1986")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()

# Part B

# Step 1: Map GPS locations in 2D image array
# January 28th
all_df = pd.merge(stationsdf, tempdf)
jan_df = all_df[(all_df['month'] == 1) & (all_df['day'] == 28)]
jan_df = jan_df[abs(jan_df['lat'] <= 50) & abs(jan_df['lat'] >= 25)]
jan_df = jan_df[abs(jan_df['long'] <= -65) & abs(jan_df['long'] >= -125)]

# February 1st
feb_df = all_df[(all_df['month'] == 2) & (all_df['day'] == 1)]
feb_df = feb_df[abs(feb_df['lat'] <= 50) & abs(feb_df['lat'] >= 25)]
feb_df = feb_df[abs(feb_df['long'] <= -65) & abs(feb_df['long'] >= -125)]

# Step 2: 3-valued RGB color np_array

# given dimensions and regulations
DIMENX = 100
DIMENY = 150
LATMIN = 25
LATMAX = 50
LONGMIN = -125
LONGMAX = -65

# From Dr.Strange's Lecture Notes
def convert_to_pos(lat, long):
    """
        Convert lat and lon to corresponding x and y
    """
    row = (lat - LATMIN) / (LATMAX - LATMIN)
    row *= DIMENX # Change to DIMENX
    row = DIMENX - row

    # col = (long-LONGMIN) - (LONGMAX - LONGMIN)
    # change to /, not -
    col = (long-LONGMIN) / (LONGMAX - LONGMIN)
    col *= DIMENY
    return (int(row), int(col))

# Specify for each month
jan_arr = np.full((DIMENX + 1, DIMENY + 1), -1000)
feb_arr = np.full((DIMENX + 1, DIMENY + 1), -1000)

# Match coordinates with temperatures
for idx, row in jan_df.iterrows():
    (x, y) = convert_to_pos(row["lat"], row["long"])
    jan_arr[x][y] = row["temp"]

for idx, row in feb_df.iterrows():
    (x, y) = convert_to_pos(row["lat"], row["long"])
    feb_arr[x][y] = row["temp"]

# 3D array for images
jan_image = np.zeros((DIMENX + 1, DIMENY + 1, 3), dtype = float)
feb_image = np.zeros((DIMENX + 1, DIMENY + 1, 3), dtype = float)

# red to dark blue (like the rainbow) = hot to cold
color = [[0,0,128], [0,0,255], [0,191,255], [64,224,208], [152,251,152], [173,255,47], [255,255,0], [255,140,0], [255,0,0], [178,34,34]]

# each range in the array is assigned a color
for i in range(jan_arr.shape[0]):
    for j in range(jan_arr.shape[1]):
        temp = jan_arr[i][j]
        if (temp >= -10) and (temp <10):
            jan_image[i][j] = color[0]
        elif (temp >= 10) and (temp <20):
            jan_image[i][j] = color[1]
        elif (temp >= 20) and (temp <30):
            jan_image[i][j] = color[2]
        elif (temp >= 30) and (temp <40):
            jan_image[i][j] = color[3]
        elif (temp >= 40) and (temp <50):
            jan_image[i][j] = color[4]
        elif (temp >= 50) and (temp <60):
            jan_image[i][j] = color[5]
        elif (temp >= 60) and (temp <70):
            jan_image[i][j] = color[6]
        elif (temp >= 70) and (temp <80):
            jan_image[i][j] = color[7]
        elif (temp >= 80) and (temp <90):
            jan_image[i][j] = color[8]
        elif (temp >= 90) and (temp <100):
            jan_image[i][j] = color[9]
        elif temp == -1000:
            jan_image[i][j] = [0,0, 0]

# each range in the array is assigned a color
for i in range(feb_arr.shape[0]):
    for j in range(feb_arr.shape[1]):
        temp = feb_arr[i][j]
        if (temp >= -10) and (temp <10):
            feb_image[i][j] = color[0]
        elif (temp >= 10) and (temp <20):
            feb_image[i][j] = color[1]
        elif (temp >= 20) and (temp <30):
            feb_image[i][j] = color[2]
        elif (temp >= 30) and (temp <40):
            feb_image[i][j] = color[3]
        elif (temp >= 40) and (temp <50):
            feb_image[i][j] = color[4]
        elif (temp >= 50) and (temp <60):
            feb_image[i][j] = color[5]
        elif (temp >= 60) and (temp <70):
            feb_image[i][j] = color[6]
        elif (temp >= 70) and (temp <80):
            feb_image[i][j] = color[7]
        elif (temp >= 80) and (temp <90):
            feb_image[i][j] = color[8]
        elif (temp >= 90) and (temp <100):
            feb_image[i][j] = color[9]
        elif temp == -1000:
            feb_image[i][j] = [0,0, 0]

# Step 3: Jan 28 & Feb 1 Image Plot
plt.figure(figsize=(10,10))
plt.title("Temperatures in the US on January 28th, 1986")
plt.ylabel("Longitude")
plt.xlabel("Latitude")
plt.imshow(jan_image, interpolation = 'none')
plt.show()

plt.figure(figsize=(10,10))
plt.title("Temperatures in the US on February 1st, 1986")
plt.ylabel("Longitude")
plt.xlabel("Latitude")
plt.imshow(feb_image, interpolation = 'none')
plt.show()
