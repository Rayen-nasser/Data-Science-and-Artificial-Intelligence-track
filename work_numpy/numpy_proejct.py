import numpy as np

# Creating an array with 15 evenly spaced values between 0 and 2
linspace_array = np.linspace(0, 2, 15)
print(linspace_array)

# Creating a 3D array
my_3d_array = np.array([
    [
        [1.1, 2.1, 3.1], [4.1, 5.1, 6.1]
    ],
    [
        [7.1, 8.1, 9.1], [10.1, 11.1, 12.1]
    ]
])

# Printing the properties of the 3D array
print(type(my_3d_array))  # <class 'numpy.ndarray'>
print(my_3d_array.dtype)  # float64
print(my_3d_array.shape)  # (2, 2, 3)
print(my_3d_array.size)   # 12
print(my_3d_array.ndim)   # 3


# Converting the 3D array to a 4D array
my_4d_array = np.array(my_3d_array, ndmin=4)
print(my_4d_array.ndim)  # 4
print(my_4d_array.shape)  # (1, 2, 2, 3)


# Converting the data type of the 4D array to int
my_new_array = my_4d_array.astype(int)
print(my_new_array.dtype)  # int64


# Iterating over the elements of the array and printing them
for x in np.nditer(my_new_array):
    print(x, end=' ')


# Accessing specific elements in the array
print(my_new_array[0, 1, 0, 1])  # 8
print(my_new_array[0, 0, 1, 1:])  # [5 6]
print(np.where(my_new_array == 8))  # (array([0]), array([1]), array([0]), array([1]))



# Reshaping the array
reshaped_array = my_new_array.reshape(2, 3, 2)
print(reshaped_array)


# Creating two 2x2 arrays
arr1 = np.array([['A', 'B'], ['E', 'F']])
arr2 = np.array([['C', 'D'], ['G', 'H']])

# Concatenating the arrays along the first axis (default)
joined_arrays = np.concatenate((arr1, arr2))
print(joined_arrays)
# Output:
# [['A' 'B']
#  ['E' 'F']
#  ['C' 'D']
#  ['G' 'H']]

# Concatenating the arrays along the second axis
joined_arrays2 = np.concatenate((arr1, arr2), axis=1)
print(joined_arrays2)
# Output:
# [['A' 'B' 'C' 'D']
#  ['E' 'F' 'G' 'H']]

# Splitting the concatenated array along the second axis
split_joined_arrays = np.array_split(joined_arrays, 2, axis=1)
print(split_joined_arrays)
# Output:
# [array([['A', 'B'],
#        ['E', 'F'],
#        ['C', 'D'],
#        ['G', 'H']], dtype='<U1'), array([], shape=(4, 0), dtype='<U1')]

