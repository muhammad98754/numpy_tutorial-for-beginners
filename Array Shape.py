#shape of an array is the number of elements in each dimension.

#Get the Shape of an Array

#Print the shape of a 2-D array:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) #(2, 4)

#The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print(arr.shape) #shape of array : (1, 1, 1, 1, 4)

