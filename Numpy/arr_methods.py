import numpy as np


#  Reshape: returns the array in a reshaped version
arr = np.arange(25) # returns an array of 25 elements
arr_shaped = arr.reshape(5, 5) # reshapes the arr into a 2-d array of 5 rows and columns resp

arr.max() # return max value
arr.min # return min value

arr.argmax() # Index location of max value. The same can be done for lowest value

# Get shape of arr
shape = arr.shape

# Get datatype
d_type = arr.dtype