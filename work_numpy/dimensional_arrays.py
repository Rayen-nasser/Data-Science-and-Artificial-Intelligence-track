import numpy as np


# 1D Array
print("\n 1D Array \n")
a = np.array([12, 52])
print(a)
print("type: ",type(a), a.dtype)
print("size:", a.size)
print("shape:", a.shape)
print("dimensional:", a.ndim)
print("item size:", a.itemsize)
print("data:", a.data)



# 2D Array
print("\n 2D Array \n")
b = np.array([
    [41,5,56],
    [13,85,6],
    [41,75,6],
])
print(b)
print("type: ",type(b), b.dtype)
print("size:", b.size)
print("shape:", b.shape)
print("dimensional:", b.ndim)
print("item size:", b.itemsize)
print("data:", b.data)


# 2D Array
print("\n 3D Array \n")
c = np.array([
    [
        [1,2,3],
        [1,2,3],
        [1,2,3]
    ],
    [
        [1,2,3],
        [1,2,3],
        [1,2,3]
    ],
    [
        [1,2,3],
        [1,2,3],
        [1,2,3]
    ]
])
print(c)
print("type: ",type(c), c.dtype)
print("size:", c.size)
print("shape:", c.shape)
print("dimensional:", c.ndim)
print("item size:", c.itemsize)
print("data:", c.data)