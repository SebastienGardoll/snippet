# conda install matplotlib
                      #### Taking 2011's Irene as an example ####

'''
@line: 48803 in hurdat2-1851-2017-050118.txt

2011 08 21 00h00 to 2011 08 30 00h00

AL092011,              IRENE,     43,

20110821, 0000,  , TS, 15.0N,  59.0W,  45, 1006,  105,    0,    0,   45,    0,    0,    0,    0,    0,    0,    0,    0,
20110821, 0600,  , TS, 16.0N,  60.6W,  45, 1006,  130,    0,    0,   80,    0,    0,    0,    0,    0,    0,    0,    0,
20110821, 1200,  , TS, 16.8N,  62.2W,  45, 1005,  130,    0,    0,   70,    0,    0,    0,    0,    0,    0,    0,    0,
20110821, 1800,  , TS, 17.5N,  63.7W,  50,  999,  130,   20,    0,   70,   30,    0,    0,    0,    0,    0,    0,    0,
20110821, 2300, L, TS, 17.8N,  64.6W,  60,  993, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999,
20110822, 0000,  , TS, 17.9N,  65.0W,  60,  993,  130,   30,   30,   90,   30,    0,    0,   30,    0,    0,    0,    0,
20110822, 0525, L, TS, 18.1N,  65.8W,  60,  990, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999,
20110822, 0600,  , HU, 18.2N,  65.9W,  65,  990,  130,   60,   60,   90,   40,   25,   20,   35,   25,    0,    0,    0,
20110822, 1200,  , HU, 18.9N,  67.0W,  70,  989,  160,   60,   60,   90,   40,   25,   20,   35,   25,    0,    0,    0,
20110822, 1800,  , HU, 19.3N,  68.0W,  75,  988,  160,   60,   40,   90,   40,   30,   20,   35,   25,    0,    0,    0,
20110823, 0000,  , HU, 19.7N,  68.8W,  80,  981,  160,   70,   50,  100,   70,   30,   30,   70,   25,    0,    0,   35,
20110823, 0600,  , HU, 20.1N,  69.7W,  80,  978,  180,  120,   90,  130,   90,   60,   40,   70,   45,   30,   20,   35,
20110823, 1200,  , HU, 20.4N,  70.6W,  80,  978,  180,  120,   90,  130,   90,   60,   40,   70,   40,   30,   20,   35,
20110823, 1800,  , HU, 20.7N,  71.2W,  80,  977,  180,  120,   90,  130,   75,   60,   40,   70,   35,   30,   20,   35,
20110824, 0000,  , HU, 21.0N,  71.9W,  80,  969,  180,  150,   90,  150,   70,   70,   40,   70,   35,   30,   25,   35,
20110824, 0600,  , HU, 21.3N,  72.5W,  95,  965,  180,  150,   90,  150,   70,   70,   40,   70,   35,   30,   25,   35,
20110824, 1200,  , HU, 21.9N,  73.3W, 105,  957,  180,  150,   90,  150,   90,   60,   45,   80,   45,   40,   25,   40,
20110824, 1600, L, HU, 22.4N,  74.0W, 100,  955, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999,
20110824, 1800,  , HU, 22.7N,  74.3W, 100,  954,  200,  180,  100,  150,  100,   70,   50,   80,   50,   45,   25,   40,
20110825, 0000, L, HU, 23.5N,  75.1W,  95,  952,  220,  180,  100,  150,  100,   90,   50,   80,   60,   60,   25,   50,
20110825, 0600,  , HU, 24.1N,  75.9W,  95,  950,  220,  180,  100,  150,  100,   80,   50,   70,   60,   60,   25,   50,
20110825, 0900, L, HU, 24.7N,  76.2W,  90,  950, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999, -999,
20110825, 1200,  , HU, 25.4N,  76.6W,  90,  950,  250,  200,  100,  160,  100,  100,   50,   70,   60,   60,   25,   50,
20110825, 1800, L, HU, 26.5N,  77.2W,  90,  950,  250,  200,  125,  160,  110,  100,   50,   75,   70,   60,   25,   50,
20110826, 0000,  , HU, 27.7N,  77.3W,  90,  946,  250,  200,  125,  160,  110,  100,   50,   75,   70,   60,   25,   50,
20110826, 0600,  , HU, 28.8N,  77.3W,  90,  942,  250,  200,  130,  175,  125,  105,   75,   75,   80,   80,   50,   50,
20110826, 1200,  , HU, 30.0N,  77.4W,  85,  947,  250,  200,  130,  175,  125,  105,   75,   75,   80,   80,   50,   50,
20110826, 1800,  , HU, 31.1N,  77.5W,  80,  950,  250,  225,  140,  175,  125,  125,   80,   75,   80,   80,   50,   50,
20110827, 0000,  , HU, 32.1N,  77.1W,  75,  952,  225,  225,  140,  140,  125,  125,   90,   75,   80,   80,   40,   40,
20110827, 0600,  , HU, 33.4N,  76.8W,  75,  952,  225,  225,  140,  140,  125,  125,   90,   75,   80,   80,   40,   40,
20110827, 1200, L, HU, 34.7N,  76.6W,  75,  952,  225,  225,  150,  125,  125,  125,   90,   60,   80,   80,   40,   35,
20110827, 1800,  , HU, 35.5N,  76.3W,  65,  950,  210,  225,  150,  125,  125,  125,   80,   60,   75,   75,   35,   35,
20110828, 0000,  , HU, 36.7N,  75.7W,  65,  951,  210,  225,  150,  125,  150,  150,   80,   60,   75,   75,    0,    0,
20110828, 0600,  , HU, 38.1N,  75.0W,  65,  958,  230,  280,  160,  110,  150,  150,   80,   30,   75,   75,    0,    0,
20110828, 0935, L, TS, 39.4N,  74.4W,  60,  959,  230,  280,  160,  110,  150,  150,   80,   30,    0,    0,    0,    0,
20110828, 1200,  , TS, 40.3N,  74.1W,  55,  963,  230,  280,  130,   50,  150,  150,   80,   30,    0,    0,    0,    0,
20110828, 1300, L, TS, 40.6N,  74.0W,  55,  965,  230,  280,  130,   50,  150,  150,   80,   30,    0,    0,    0,    0,
20110828, 1800,  , TS, 42.5N,  73.1W,  50,  970,  230,  280,  180,   50,  150,  150,   80,   30,    0,    0,    0,    0,
20110829, 0000,  , EX, 44.2N,  72.1W,  45,  979,  230,  315,  250,   50,    0,    0,    0,    0,    0,    0,    0,    0,
20110829, 0600,  , EX, 46.5N,  69.5W,  40,  983,  360,  360,  360,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20110829, 1200,  , EX, 49.1N,  66.7W,  40,  985,  360,  360,  300,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20110829, 1800,  , EX, 51.3N,  63.8W,  40,  987,    0,  360,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
20110830, 0000,  , EX, 53.0N,  60.0W,  40,  991,    0,  270,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
'''

from netCDF4 import Dataset

import os.path as path

from matplotlib import pyplot as plt

import numpy as np

import re

import math

# NetCDF resolution.
TIME_SAMPLING = 4
LAT_RESOLUTION = 0.25
LON_RESOLUTION = 0.25

NUM_DECIMAL_LAT = 2
NUM_DECIMAL_LON = 2

# Tensor resolution. Must be even numbers.
X_RESOLUTION = 32
Y_RESOLUTION = 32

# Pattern matching expressions.
LATITUDE_PATTERN = re.compile('(\d+(?:\.\d+)?)([NS])')
LONGITUDE_PATTERN = re.compile('(\d+(?:\.\d+)?)([WE])')

HOUR_TIME_STEP_MAPPING = {'0000':0, '0600':1, '1200':2, '1800':3}

# num_day starts at 1 .
# time_step starts at zero.
def compute_time_index(num_day, time_step = 0):
  if(time_step >= TIME_SAMPLING):
    days_to_add = int(time_step / TIME_SAMPLING)
    time_step = time_step % TIME_SAMPLING
    num_day = num_day + days_to_add
  return TIME_SAMPLING*(num_day-1) + time_step

# units: degrees_north
# index zero       =>  90° <=> 90°N
# last index (720) => -90° <=> 90°S 
def compute_lat_index(lat):
  return int(360 - (lat/LAT_RESOLUTION))

# units: degrees_east
# index zero        =>   0° <=> 180°W or -180
# last index (1440) => 360° <=> 180°E or  180
def compute_lon_index(lon):
  return int((math.fmod((360+lon), 360))/LON_RESOLUTION)

def parse_lat(lat_string):
  match = LATITUDE_PATTERN.match(lat_string)
  if match:
    result = float(match.group(1))
    if match.group(2) == 'S':
      result = -result
    return result
  else:
    raise AttributeError("unsupported format of latitude (%s)"%(lat_string))

def parse_lon(lon_string):
  match = LONGITUDE_PATTERN.match(lon_string)
  if match:
    result = float(match.group(1))
    if match.group(2) == 'W':
      result = -result
    return result
  else:
    raise AttributeError("unsupported format of latitude (%s)"%(lon_string))

def parse_hour(hour_literal):
  result = HOUR_TIME_STEP_MAPPING[hour_literal]

def round_nearest(value, resolution, num_decimal):
    return round(round(value / resolution) * resolution, num_decimal)

parent_dir_path = '/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_SF/2011'
filename = 'msl.201108.ashe5.GLOBAL_025.nc'

if X_RESOLUTION % 2 != 0:
  raise Exception("x resolution is not even")

if Y_RESOLUTION % 2 != 0:
  raise Exception("y resolution is not even")

half_x_frame = int(X_RESOLUTION*LON_RESOLUTION / 2)
half_y_frame = int(Y_RESOLUTION*LAT_RESOLUTION / 2)

file_path = path.join(parent_dir_path, filename)
# dimensions(sizes): longitude(1440), latitude(721), time(124)
nc_dataset = Dataset(file_path, 'r')

num_day = 25
time_step = 3

lat = round_nearest(parse_lat("26.5N"), LAT_RESOLUTION, NUM_DECIMAL_LAT)
lon = round_nearest(parse_lon("77.2W"), LON_RESOLUTION, NUM_DECIMAL_LON)

print(lat)
print(lon)

time_min_index =  compute_time_index(num_day, time_step) # 80 => 1855152
time_max_index =  time_min_index + 1 # 81

# latitudes are stored inverted.
lat_min_index  = compute_lat_index((lat + half_y_frame))
lat_max_index  = compute_lat_index((lat - half_y_frame))

lon_min_index  = compute_lon_index((lon - half_x_frame)) # -63
lon_max_index  = compute_lon_index((lon + half_x_frame)) # -55

print(lat_min_index) # 238
print(lat_max_index) # 270
print(lon_min_index) # 1115
print(lon_max_index) # 1147


# float32 msl(time, latitude, longitude)
msl_selected_region = nc_dataset['msl'][time_min_index:time_max_index, lat_min_index:lat_max_index, lon_min_index:lon_max_index][0]

# print(msl_selected_region)

plt.figure()
plt.imshow(msl_selected_region,cmap='gist_rainbow_r',interpolation="none")
plt.show()

""" 
Intercomparison:
ferret
use "/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_SF/2011/msl.201108.ashe5.GLOBAL_025.nc"
set region/x=81.25W:73.25W/y=22.5N:30.5N/t=1855266/k=1
shade msl

set region/x=174W:166W/y=76N:84N/t=1855152/k=1
shade msl
#lon = -170
#lat = 80

set region/x=174W:166W/y=76S:84S/t=1855152/k=1
shade msl
#lon = -170
#lat = -80

set region/x=166E:174E/y=76S:84S/t=1855152/k=1
shade msl
#lon = 170
#lat = -80

set region/x=166E:174E/y=76N:84N/t=1855152/k=1
shade msl
#lon = 170
#lat = 80
"""


latitude_indexes = dict()

for index in range(0, len(nc_dataset.variables["latitude"])):
  latitude_indexes[nc_dataset.variables["latitude"][index].data.item(0)] = index

longitude_indexes = dict()

for index in range(0, len(nc_dataset.variables["longitude"])):
  _lon = nc_dataset.variables["longitude"][index].data.item(0)
  if _lon > 180.0:
    _lon = _lon -360.0
  longitude_indexes[_lon] = index

# print(longitude_indexes[lon])
# print(compute_lon_index(lon))

lat_min_index  = latitude_indexes[(lat + half_y_frame)]
lat_max_index  = latitude_indexes[(lat - half_y_frame)]
lon_min_index  = longitude_indexes[(lon - half_x_frame)]
lon_max_index  = longitude_indexes[(lon + half_x_frame)]

print(lat_min_index) # 238
print(lat_max_index) # 270
print(lon_min_index) # 1115
print(lon_max_index) # 1147

# float32 msl(time, latitude, longitude)
msl_selected_region = nc_dataset['msl'][time_min_index:time_max_index, lat_min_index:lat_max_index, lon_min_index:lon_max_index][0]

# print(msl_selected_region)

plt.figure()
plt.imshow(msl_selected_region,cmap='gist_rainbow_r',interpolation="none")
plt.show()

print("%d : %d"%(compute_lat_index(80), latitude_indexes[80]))
print("%d : %d"%(compute_lat_index(-80), latitude_indexes[-80]))

print("%d : %d"%(compute_lon_index(170), longitude_indexes[170]))
print("%d : %d"%(compute_lon_index(-170), longitude_indexes[-170]))

# --------
parent_dir_path = '/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_PL/2011'
filename = 'v.201108.aphe5.GLOBAL_025.nc'
file_path = path.join(parent_dir_path, filename)
nc_dataset = Dataset(file_path, 'r')

v_indexes = dict()

for index in range(0, len(nc_dataset.variables["level"])):
  v_indexes[nc_dataset.variables["level"][index].data.item(0)] = index

v_index = v_indexes[850]

# float32 v(time,level,latitude,longitude)
v_selected_region = nc_dataset['v'][time_min_index:time_max_index, v_index, lat_min_index:lat_max_index, lon_min_index:lon_max_index][0]
plt.figure()
plt.imshow(v_selected_region,cmap='gist_rainbow_r',interpolation="none")
plt.show()

"""
ferret
use "/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_PL/2011/v.201108.aphe5.GLOBAL_025.nc"
set region/x=81.25W:73.25W/y=22.5N:30.5N/t=1855266/k=31
shade v
"""

parent_dir_path = '/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_PL/2011'
filename = 'u.201108.aphe5.GLOBAL_025.nc'
file_path = path.join(parent_dir_path, filename)
nc_dataset = Dataset(file_path, 'r')

u_indexes = dict()

for index in range(0, len(nc_dataset.variables["level"])):
  u_indexes[nc_dataset.variables["level"][index].data.item(0)] = index

u_index = u_indexes[850]

# float32 v(time,level,latitude,longitude)
u_selected_region = nc_dataset['u'][time_min_index:time_max_index, u_index, lat_min_index:lat_max_index, lon_min_index:lon_max_index][0]
plt.figure()
plt.imshow(u_selected_region,cmap='gist_rainbow_r',interpolation="none")
plt.show()
"""
ferret
use "/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_PL/2011/u.201108.aphe5.GLOBAL_025.nc"
set region/x=81.25W:73.25W/y=22.5N:30.5N/t=1855266/k=31
shade u
"""

parent_dir_path = '/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_PL/2011'
filename = 'ta.201108.aphe5.GLOBAL_025.nc'
file_path = path.join(parent_dir_path, filename)
nc_dataset = Dataset(file_path, 'r')

ta_indexes = dict()

for index in range(0, len(nc_dataset.variables["level"])):
  ta_indexes[nc_dataset.variables["level"][index].data.item(0)] = index

ta_index = ta_indexes[200]

# float32 v(time,level,latitude,longitude)
ta_selected_region = nc_dataset['ta'][time_min_index:time_max_index, ta_index, lat_min_index:lat_max_index, lon_min_index:lon_max_index][0]
plt.figure()
plt.imshow(ta_selected_region,cmap='gist_rainbow_r',interpolation="none")
plt.show()
"""
ferret
use "/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_PL/2011/ta.201108.aphe5.GLOBAL_025.nc"
set region/x=81.25W:73.25W/y=22.5N:30.5N/t=1855266/k=15
shade ta
"""

ta_index = ta_indexes[500]

# float32 v(time,level,latitude,longitude)
ta_selected_region = nc_dataset['ta'][time_min_index:time_max_index, ta_index, lat_min_index:lat_max_index, lon_min_index:lon_max_index][0]
plt.figure()
plt.imshow(ta_selected_region,cmap='gist_rainbow_r',interpolation="none")
plt.show()
"""
ferret
use "/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_PL/2011/ta.201108.aphe5.GLOBAL_025.nc"
set region/x=81.25W:73.25W/y=22.5N:30.5N/t=1855266/k=22
shade ta
"""

# Build -180 to 180 longitude scale to degrees east (0 to 359.75)
longitude_convert = dict()

for index in range(0, len(nc_dataset.variables["longitude"])):
  _lon_de = nc_dataset.variables["longitude"][index].data.item(0)
  if _lon_de > 180.0:
    _lon = _lon_de -360.0
  else:
    _lon = _lon_de
  longitude_convert[_lon] = _lon_de

import os.path as path
dataset_parent_dir_path='/data/sgardoll/cyclone_data.clean/dataset'

latitude_indexes_file_path=path.join(dataset_parent_dir_path, 'latitude_indexes')
np.save(file=latitude_indexes_file_path, arr=latitude_indexes, allow_pickle=False)

longitude_indexes_file_path=path.join(dataset_parent_dir_path, 'longitude_indexes')
np.save(file=longitude_indexes_file_path, arr=longitude_indexes, allow_pickle=False)

longitude_convert_file_path=path.join(dataset_parent_dir_path, 'longitude_convert')
np.save(file=longitude_convert_file_path, arr=longitude_convert, allow_pickle=False)

v_indexes_file_path=path.join(dataset_parent_dir_path, 'v_indexes')
np.save(file=v_indexes_file_path, arr=v_indexes, allow_pickle=False)

u_indexes_file_path=path.join(dataset_parent_dir_path, 'u_indexes')
np.save(file=u_indexes_file_path, arr=u_indexes, allow_pickle=False)

ta_indexes_file_path=path.join(dataset_parent_dir_path, 'ta_indexes')
np.save(file=ta_indexes_file_path, arr=ta_indexes, allow_pickle=False)


nc_dataset.close()