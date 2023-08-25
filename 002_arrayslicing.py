import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# arr[start:end:step]
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1
# If we pass n as the end, n is excluded from the slice

print(arr[4:])
print(arr[:4])

print(arr[4:7])
print(arr[-6:-3])

print(arr[1:5:2])
print(arr[::2])

print("\n",arr2[0:2, 1:4])