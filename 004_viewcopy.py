import numpy as np

# Copy is a new array, and View is just a view of the original array.

# The Copy owns the data and any changes in copy will not affect original array, vice-versa.

# The View doesn't own the data and any changes in view will affect the original array, vice-versa.

arr = np.array([1,2,3,4,5])
arr2 = np.array([[0,1,2,3,4],
                [5,6,7,8,9]])

arr_copy = arr.copy()

arr_view = arr.view()

print(f"Before Changes: {arr}")
arr[0] = 0
print(f"After Changes: {arr}")

print(f"Array Copy: {arr_copy}")

print(f"Array View: {arr_view}")

#As we can notice in the output, the changes in arr are reflected in arr_view but not in arr_copy.

print(arr_copy.base) #Returns None as copy owns the data
print(arr_view.base) #Returns arr as view doesn't own the data

print(f"\nShape of arr: {arr2.shape}")
# Shape of arr: (2, 5)
# Dimension:     2, 1
# Here, (x,y) represents no. of items in each dimension.
# x=2 represents 2 items in 2D (2 rows)
# y=5 represents 5 items in 1D (5 elements in 1 row)

arr3 = np.array([1,2,3,4], ndmin=5)
print(f"Shape: {arr3.shape}")

# Shape: (1, 1, 1, 1, 4)
# Dim:    5  4  3  2  1
# 1D has 4 items because there's only 4 items in the innermost fields of the array