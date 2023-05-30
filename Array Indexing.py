#Access Array Elements

import numpy as np
a=np.array([1,2],ndmin=7)
print(a)
print(a.ndim)
print(a[0,0,0,0,0,0,1])

#output is 2


#we can use this method of calling for 1D array

import numpy as np
a=np.array([1, 2, 3, 4])
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[-1])
print(a[0:len(a)])
print(a[:])
print(a[0]+a[2])

#Access 2-D Arrays

#Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

import numpy as np
a=np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a[0,2]) #output is 3
print(a[1,3]) #output is 9
print(a[:,2:3]) 
print(a[:,:])  #for full array

#Access 3-D Arrays

#Access the third element of the second array of the first array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

#Negative Indexing

#Print the last element from the 2nd dim:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])



