#Checking the Data Type of an Array

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype) #int32

import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype) #U6  U - unicode string


#Creating Arrays With a Defined Data Type

import numpy as np

arr = np.array(['apple', 'banana', 'cherry'],dtype="S")

print(arr.dtype)

import numpy as np

arr = np.array(['app', 'bana', 'ch'],dtype="U")

print(arr.dtype) #output is U4

import numpy as np

arr = np.array(['app', 'bana', 'ch'],dtype="S")

print(arr.dtype) #output is S4

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i8') 

print(arr)
print(arr.dtype) #output is int64

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)#output is int32

#Converting Data Type on Existing Arrays

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype("i")

print(newarr)
print(newarr.dtype) #int32

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype("U")

print(newarr) #['1.1' '2.1' '3.1']
print(newarr.dtype) #U32

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype("S")

print(newarr)#[b'1.1' b'2.1' b'3.1']
print(newarr.dtype)#S32

#Change data type from integer to boolean:
import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)




