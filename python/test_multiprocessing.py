import numpy as np
import multiprocessing as mp
import ctypes
import sys
from multiprocessing import Pool

import time
start = time.time()

is_debug      = False
has_to_save   = bool(sys.argv[3])

num_images    = int(sys.argv[1])
num_channel   =     8
x_pixel_size  =    32
y_pixel_size  =    32
num_processes = int(sys.argv[2])

image_range   = range(0, num_images)
channel_range = range(0, num_channel)
y_pixel_range = range(0, y_pixel_size)
x_pixel_range = range(0, x_pixel_size)
glob = 10
# Static allocation of the tensor
shared_tensor = mp.RawArray(ctypes.ARRAY(ctypes.ARRAY(ctypes.ARRAY(ctypes.c_double, x_pixel_size), y_pixel_size), num_channel), num_images)

def fill_tensor(image_index):
  for channel_index in channel_range:
    for y_pixel_index in y_pixel_range:
      for x_pixel_index in x_pixel_range:
        shared_tensor[image_index][channel_index][y_pixel_index][x_pixel_index] = image_index + glob
  return None

if num_processes == 1:
  for image_index in image_range:
    fill_tensor(image_index)
else:
  with Pool(processes = num_processes) as pool:
    pool.map(fill_tensor, image_range)

stop = time.time()

print("spend %f seconds filling the tensor"%((stop-start)))

start = stop
if has_to_save:
  numpy_wrapping = np.ctypeslib.as_array(shared_tensor)
  np.save(file="/home/sgardoll/tmp/test", arr=numpy_wrapping, allow_pickle=True)

stop = time.time()

print("spend %f seconds saving the tensor on disk"%((stop-start)))

