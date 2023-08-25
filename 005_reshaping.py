import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3) # Reshaped to 4 rows, 3 items per row

print(newarr)

print(newarr.reshape(1,12)) # Reshaped to 1 row, 12 items

# Both of these give the same output
print(newarr.reshape(6,2))
print(arr.reshape(6,2))

print()

print(arr.reshape(2,2,3))
print(arr.reshape(2,2,3).base) #Returns the original array so it is a view

print(arr.reshape(3,2,-1)) # Here, -1 represents unknown value. Numpy will automatically fill this value for us

print(f"\nFlattened Array: {newarr.reshape(-1)}")