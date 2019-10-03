Code avec Xarray :

#%%
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:23:41 2018

@author: Sébastien Gardoll
"""

import xarray as xr
import math

netcdf_file_path = '/bdd/ECMWF/ERA5/NETCDF/GLOBAL_025/4xdaily/AN_SF/2011/msl.201108.ashe5.GLOBAL_025.nc'

nc_dataset = xr.open_dataset(netcdf_file_path)
#nc_dataset.info()
'''
xarray.Dataset {
dimensions:
  latitude = 721 ;
  longitude = 1440 ;
  time = 124 ;

variables:
  float32 longitude(longitude) ;
    longitude:units = degrees_east ;
    longitude:long_name = longitude ;
  float32 latitude(latitude) ;
    latitude:units = degrees_north ;
    latitude:long_name = latitude ;
  datetime64[ns] time(time) ;
    time:long_name = time ;
  float32 msl(time, latitude, longitude) ;
    msl:units = Pa ;
    msl:long_name = Mean sea level pressure ;
    msl:standard_name = air_pressure_at_sea_level ;
    msl:level_desc = surface ;

// global attributes:
  :Conventions = CF-1.6 ;
  :title = ERA5 reanalysis ;
  :data_type = 4xdaily fields in analysis ;
  :grid_resolution_in_degrees = 0.30000001192092896 ;
  :source = credit: ECMWF, COPERNICUS Climate Change Service data, available from the ESPRI/IPSL data center ;
  :NCO = "4.6.1" ;
  :history = Mon Mar 19 05:54:00 2018: ncatted -a history,global,d,, /scratch/ms/fr/lmi/ERA5/AN_SF/2011/msl.201108.ashe5.GLOBAL_025.nc ;
}
'''

year = 2011
month = 8
day = 21
hour = 'T00:00:00.000000000'
lat = 15
lon = -60

HALF_LAT_FRAME = 4
HALF_LON_FRAME = 4
LAT_RESOLUTION = 0.25
LON_RESOLUTION = 0.25

# Lat is inverted => @see loc call.
# Must deal with open range (-0.25) because slice is inclusive.
lat_min  = (lat - HALF_LAT_FRAME + LAT_RESOLUTION)
lat_max  = (lat + HALF_LAT_FRAME)

# Should be precalculated in dictionary or try interpolate.
# Must deal with open range (-0.25) because slice is inclusive.
lon_min  = lon - HALF_LON_FRAME
lon_max  = lon + HALF_LON_FRAME - LON_RESOLUTION

# Convert lon into degrees_east
lon_min  = math.fmod((360+lon_min), 360)
lon_max  = math.fmod((360+lon_max), 360)

# Must deal with open range (-0.25) because slice is inclusive.
nc_dataset.loc[dict(time=f'{year}-{month}-{day}{hour}', latitude=slice(lat_max, lat_min), longitude=slice(lon_min, lon_max))]
# Equivalent.
extracted_region = nc_dataset.sel(time=f'{year}-{month}-{day}{hour}', latitude=slice(lat_max, lat_min), longitude=slice(lon_min, lon_max))

print(extracted_region)
