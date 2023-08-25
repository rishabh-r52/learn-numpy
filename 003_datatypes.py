import numpy as np

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

arr = np.array([1,2,3,4,5], dtype="i4")

print(arr.dtype)
print(arr)

arr2 = arr.astype('S') #Changes type to String

print(arr2.dtype)
print(arr2)

farr = np.array([1.1,2.2,3.3,0.0,7.7,8.8,9.9])

print(farr)

iarr = farr.astype(int) #Changes type to integer

print(iarr)

barr = farr.astype(bool) #Changes type to bool

print(barr)