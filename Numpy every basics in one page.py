#intro to numpy

import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
print(np1)
np2=np.arange(1,10,1)
print(np2)
print(np2.shape)
np3=np.zeros((2,10))
print(np3)
print(np3.shape)
np4=np.full((2,1),6)
print(np4.shape)
np5=list([1,2,5,6])
print(np.array(np5)[3])
------------------------------------------------

#slicing numpy arrays

import numpy as np
np1=np.array([1,2,3,4,5,6,7,8,9])
print(np.where(np1==5))
print(np.where(np1==2))
print(np1[1:5])
print(np1[1:])
print(np1[-10:-1])
print(np.where(np1==9))
print(np1[1:9:2])
print(np1[::2])
np2=np.array([np.arange(1,6),np.arange(6,11)])
print(np2)
np3=np.array([[ 1 , 2 ,3  ,4 , 5],
 [ 6 , 7 , 8 , 9, 10]])
print(np3[:,3:5])
print(np.where(np3==8))
------------------------------------------------
#universal functions

import numpy as np
np1=np.arange(10)
print(np1)
print(np.sqrt(np1))
print(np.array(np1**2))
print(np.absolute(np1))
np2=np.array([5, 1 ,2 ,3, 0 ,-5, 6 ,7 ,8, -9])
print(np.absolute(np2))
np3=np.arange(10)*-1
print(np.absolute(np3))
print(np1)
print(np.exp(np1))
print(np.max(np2))
print(np.min(np2))
print(np.sign(np2))
print(np.sin(np1))
print(np.cos(np2))
print(np.log(np2))
----------------------------------------------------------

#copy vs view

import numpy as np
np1=np.arange(10)


np2=np1.copy()

print(f"orginal array{np1}")
print(f"copied array{np2}")

np3=np1.view()
print(np3)
np3[0]=42
print(f"viewed array{np3}")
print(f"original array{np1}")
-------------------------------------------------------------

#draw circle using numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
r=5
centre_x=0
centre_y=0
angle=np.linspace(0,2*np.pi,361)
print(angle.shape)

x=centre_x+r*np.cos(angle)
y=centre_y+r*np.sin(angle)
print(x.shape)
print(y.shape)
plt.plot(x,y)
plt.axis("equal")
plt.show()
--------------------------------------------------------

#shape and reshape arrays

import numpy as np

np1=np.arange(1,14)
np2=np1.view().reshape(-1,13)
print(np1)
print(np2)
print(np1.shape)
print(np2.shape)

np3=np.arange(12).reshape(2,3,2)
print(np3)
print(np3.shape)
np4=np3.reshape(-1)
print(np4)
print(np4.shape)
----------------------------------------------------------

#iteration in numpy array

import numpy as np

np1=np.arange(12).reshape(-1,2,2)
#print(np1)
for (i,j) in np1:
    #print((i,j))
    for k in np.array((i,j)).reshape(-1):
        print(k)

#or in a single line print all

np2=np.arange(12).reshape(-1,3,2)
print(np2)
for i in np2.reshape(-1):
    print(i)


#using np.nditer
for i in np.nditer(np2):
    print(i)

-----------------------------------------------------------------

#rectangle using numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt


x=np.arange(0,5)
print(x.shape)
y=np.arange(0,5)

plt.plot(np.zeros(x.shape),y)
plt.plot(np.zeros(x.shape)+x.shape-1,y)
plt.plot(x,np.zeros(y.shape))
plt.plot(x,np.zeros(y.shape)+y.shape-1)
plt.show()
-------------------------------------------------------------------

#sorting numpy arrays

import numpy as np
np1=np.array([10,5,4,1,3,2,5,6])
print(np1)
print(np.sort(np1))

np2=np.array(["safeer","james","daniel","manuel"])
print(np.sort(np2))


np3=np.array([np.arange(0,6,1
                        ),np.arange(8,14)])
print(np.sort(np3))


--------------------------------------------------------------------

#searching numpy ararys

import numpy as np

np1=np.array([3,5,4,5,8,55])
x=np.where(np1==5)
print(x)
print(np1[x])
print(np1[x[0][0]])

y=np.where(np1 % 2 ==0)
print(y)
print(np1[y])

z=np.where(np1 % 2 ==1)
print(z)
print(np1[z])
print(z[0])
---------------------------------------------------------------------

#filter numpy arrays


import numpy as np

np1=np.arange(10)
print(np1.shape)
x=[True,True,False,False,False,False,False,False,False,False]
print(np1)
print(np1[x])


#or we can do in another way

new_array=[]
for i in np1:
    if i %2==0:
        new_array.append(True)
    else:
        new_array.append(False)

print(np1)
print(new_array)
print(np1[new_array])

new_array=[]
for i in np1:
    if i >5:
        new_array.append(True)
    else:
        new_array.append(False)

print(np1)
print(new_array)
print(np1[new_array])


#shortcut
x=np1 <=5
print(np1)
print(x)
print(np1[x])

