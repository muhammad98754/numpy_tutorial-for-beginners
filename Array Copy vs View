#copy is a new array, and the view is just a view of the original array

#COPY:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr) #[42  2  3  4  5]
print(x) #[1 2 3 4 5]

#VIEW:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x=arr.view()
arr[0]=42
print(arr)#[42  2  3  4  5]
print(x) #[42  2  3  4  5]



#Check if Array Owns its Data,Every NumPy array has the attribute base that returns None if the array owns the data.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base) #None
print(y.base)

#The copy returns None.
#The view returns the original array.
