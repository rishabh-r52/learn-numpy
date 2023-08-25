import numpy as np

#0D Array - A single item
arr0 = np.array(52)

#1D Array - A single list containing multiple individual items
arr1 = np.array([1,2,3,4,5]) 

#2D Array - A list containing 2 lists
arr2 = np.array([[1,2,3,4,5],
               [7,8,9,10,11]])

arr3 = np.array([[[10,-10],
                  [20,-20]],
                 [[30,-30],
                  [40,-40]]])

# We can also write it as: (for better visualization of n-dimensions)
# arr3 = np.array([ # 3rd dimension
#                     [ # 2nd dimension
#                         [ # 1st dimension
#                           10, # 0th dimension
#                          -10
#                         ],
#                         [
#                           20,
#                          -20
#                         ]
#                     ],

#                     [[30,-30],[40,-40]]
#                 ])

print(arr0)
print(type(arr0), "\n") # class - numpy.ndarray

print(arr1)
print(type(arr1), "\n") # class - numpy.ndarray

print(arr2)
print(type(arr2), "\n") # class - numpy.ndarray

print(arr3)
print(type(arr3)) # class - numpy.ndarray
print(arr3.ndim)

print("\n",np.__version__) # 1.25.2

print(arr1.shape) # (2,5)
print(arr1.size) # 10
print(arr1.dtype) # int32
print(arr1.ndim) # 2

print(arr1.flags) 
#   C_CONTIGUOUS : True
#   F_CONTIGUOUS : False
#   OWNDATA : True
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False

arr5 = np.array([1,2,3,4,5], ndmin=5)

print(arr5, f"\nNo. of Dimensions: {arr5.ndim}")

print(f"\n(0D) Element 1 (1D) of List 0 (2D) of List 1 (3D) of the 3D Array: {arr3[1,0,1]}")

print(f"\nLast element from 2D: {arr2[1,4]}") # Positive Indexing
print(f"Last element from 2D: {arr2[1,-1]}") # Negative Indexing

