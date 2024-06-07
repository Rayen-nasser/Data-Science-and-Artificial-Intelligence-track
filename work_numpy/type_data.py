import numpy as np

# Complex Data Type Array
x = np.array([2.55, 3.55], dtype=complex)
x_dtype = x.dtype

# String Data Type Array
y = np.array(["hello", "rayen", "how are you?"])
y_dtype = y.dtype

# Mixed Data Type Array
w = np.array([True, "rayen", 5, 0.2])
w_dtype = w.dtype

# Ones Array
ones_array = np.ones((3, 1))

# Range Array
range_array = np.arange(0, 20, 2)

# Linspace Array
linspace_array = np.linspace(0, 20, 5)

# Random Arrays
random_array = np.random.random((2, 2))
randn_array = np.random.randn(2, 1)
rand_array = np.random.rand(2, 2)
randint_array = np.random.randint(3, 12, (2, 2))

# Full Array
full_array = np.full((4, 4), [1, 2, 3, 4])

# Identity Matrix
eye_matrix = np.eye(5)

# Empty Array
empty_array = np.empty([3, 2], dtype=int)

# Reshaping and Transposing
a = np.arange(0, 12)
a_reshaped = a.reshape((3, 4))
a_raveled = a_reshaped.ravel()
a_transposed = a_reshaped.transpose()

# Array Operations
b = a_reshaped + 6
a_reshaped += 4
a_after_add = a_reshaped.copy()
a_reshaped *= 2
a_after_multiply = a_reshaped.copy()
multiply_result = np.multiply(a_reshaped, b)

print(x_dtype, y_dtype, w_dtype, ones_array, range_array, linspace_array,
 random_array, randn_array, rand_array, randint_array, full_array,
 eye_matrix, empty_array, a, a_reshaped, a_raveled, a_transposed,
 a_after_add, a_after_multiply, multiply_result)
