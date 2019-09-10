import numpy as np


# Create an arr
arr = np.arange(0, 11)

# Index first three items
indexed = arr[:3]

# Everything but the first three
indexed = arr[:-3] # also arr[3:]

# The same is implemented as in Lists

"""
Arrays always refer to the original array.
Copy of the array is only created when explicitly defined
as shown below
"""

copy_arr = arr.copy()


"""
Indexing 2D arrays
"""

arr_2d = np.array([[3,5,7], [34,6,78], [12,52,25]])

# Grab the element in the first row and first column: DOUBLE BRACKET NOTATION
arr_2d[0][0]
arr_2d[0] # entire row

# SINGLE BRACKET NOTATION
arr_2d[0, 2]

# Grabbing part of the 2D array
part_of_array = arr_2d[:2, 1:] # Grab everything before 3rd row and everything after the 1st column