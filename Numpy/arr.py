import numpy as np

my_mat = [[1,2,3], [4,5,6], [7,8,9]]

# Casting the list of lists to a multidimensional array:

my_arr = np.array(my_mat)

# Using Numpy built-in features to create arrays:

arr = np.arange(0, 10) # 0 - beginning, 10 - upto but not including (same as list's range)
# Array of zeros:
arr = np.zeros(4) # returns an array of four items, all zeros
arr = np.zeros((3, 5)) # array of all zeros with 3 rows by 5 columns
# The same can be done for an array of 1's

# Linspace: returns evenly y spaced arrays elements from n to p (n, p, y)
arr = np.lispace(0, 5, 10) # 10 evenly spaced items, from 0 to 5

# Identity Matrix: np.eye(n) where n is the size of the matrix; example
arr = np.eye(4)

# random
arr = np.random.rand(5) # 1-d
arr = np.random.rand(5, 5) # 2-d

# Returning numbers from a standard normal distribution centered around 0
arr = np.random.randn(2) # 1-d
arr = np.random.randn(2,4) # 2-d

# Returning random integers from a low to a high number: (low, high, count), example
arr = np.random.randint(2, 200, 10) # Inclusive on the low end and exclusive on he high end
