import numpy as np

#1D Array - A single list containing individual items
arr = np.array([1,2,3,4,5]) 

#2D Array - A list containing 2 lists
arr = np.array([[1,2,3,4,5],
               [7,8,9,10,11]])

print(arr)

print(type(arr)) # class - numpy.ndarray

print(np.__version__) # 1.25.2

print(arr.shape) # (2,5)
print(arr.size) # 10
print(arr.dtype) # int32
print(arr.ndim) # 2

print(arr.flags) 
#   C_CONTIGUOUS : True
#   F_CONTIGUOUS : False
#   OWNDATA : True
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False