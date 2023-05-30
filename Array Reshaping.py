#By reshaping we can add or remove dimensions or change number of elements in each dimension.

#Reshape From 1-D to 2-D

#Convert the following 1-D array with 12 elements into a 2-D array.

#The outermost dimension will have 4 arrays, each with 3 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
x=arr.reshape(4,3)
print(x)

#Reshape From 1-D to 3-D
#Convert the following 1-D array with 12 elements into a 3-D array.

#The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
x=arr.reshape(2,3,2)
print(x)

#Check if the returned array is a copy or a view:

print(x.base) #it is a view

#You are allowed to have one "unknown" dimension.

#pass -1 as the value, and NumPy will calculate this number for you.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
x=arr.reshape(2,3,-1)
print(x) #for above example

#Convert 1D array with 8 elements to 3D array with 2x2 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)


#converting a multidimensional array into a 1D array.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
x=arr.reshape(-1)
print(x)

#Can We Reshape Into any Shape?
#Yes, as long as the elements required for reshaping are equal in both shapes.
