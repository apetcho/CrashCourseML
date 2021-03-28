#!/usr/bin/env python3
import numpy as np


#######################
# Numpy Crash Course
#######################
# 1- Array creation
# 1.1 Conversion from other Python structures

def create_nparray():
    #
    a1D = np.array([1, 2, 3, 4])
    a2D = np.array([[1, 2], [3, 4]])
    a3D = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]])
    print(f"a1D = {a1D}\na2D = {a2D}\na3D = {a3D}")

# create_nparray()

## Specifying data type.

def nparray_dtype():
    aInt8 = np.array([127, 128, 129], dtype=np.int8)
    aUInt32 = np.array([2, 3, 4], dtype=np.uint32)
    bUInt32 = np.array([5, 6, 7], dtype=np.uint32)
    cUInt32 = aUInt32 - bUInt32
    cInt32 = aUInt32 - bUInt32.astype(np.int32)
    print(f"  aInt8 = {aInt8}")
    print(f"cUint32 = {cUInt32, cUInt32.dtype}")
    print(f" cInt32 = {cInt32, cInt32.dtype}")
    
# nparray_dtype()

# 1.2 Intrinsic NumPy array creation functions
## 1D arrays

def nparray_creation_with_intrinsic_1d():
    x = np.arange(10)
    y = np.arange(2, 10, dtype=float)
    z = np.arange(2, 9, 0.1)
    print(f"x = {x}\ny = {y}\nz = {z}")
    print(f"\n\n{np.linspace(1., 4., 6)}")
  

# nparray_creation_with_intrinsic_1d()

## 2D arrays

def create_2d_array_with_intrinsics():
    # np.eye(), np.diag(), np.vander()
    print("-- np.eye:")
    x = np.eye(3)
    y = np.eye(3, 5)
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"-- np.diag:")
    x = np.diag([1, 2, 3])
    y = np.diag([1, 2,3], 1)
    print(f"x = {x}")
    print(f"y = {y}")
    a = np.array([[1, 2], [3, 4]])
    adiag = np.diag(a)
    print(f"a = {a}\na_diag = {adiag}")
    print(f"-- np.vander")
    print(f"np.vander(np.linspace(0, 2, 5), 2):\n\n{np.vander(np.linspace(0, 2, 5), 2)}")
    print(f"np.vander([1, 2, 3, 4], 2):\n\n{np.vander([1, 2, 3, 4], 2)}")
    print(f"np.vander((1, 2, 3, 4), 4):\n\n{np.vander((1, 2, 3, 4), 4)}")

#create_2d_array_with_intrinsics()

## general ndarray creation functions

def general_ndarray_creation():
    # np.ones, np.zeroes, np.random.Generator.random, ...
    print("-- np.zeros:")
    print(f"np.zeros((2, 3)):\n{np.zeros((2, 3))}")
    print(f"np.zeros((2, 3, 2)):\n{np.zeros((2, 3, 2))}")
    print("-- np.ones:")
    print(f"np.ones((2, 3)):\n{np.ones((2, 3))}")
    print(f"np.ones((2, 3, 2)):\n{np.ones((2, 3, 2))}")
    #import numpy.random.default_rng     # as default_rng
    print(f"default_rng(42).random((2, 3)):\n{np.random.default_rng(42).random((2, 3))}")
    print(f"default_rng(42).random((2, 3, 2)):\n{np.random.default_rng(42).random((2, 3, 2))}")
    print("-- np.indices:")
    print(f"np.indices((3, 3)):\n{np.indices((3, 3))}")
    



general_ndarray_creation()
    
# --
# ndarray.ndim, ndarray.shape, ndarray.size, ndarray.dtype, ndarray.itemsize,
# ndarray.data

# 1.3 Replicating, joining, or mutating existing arrays
# 1.4 Reading arrays from disk, either from standard or custom formats
# 1.5 Creating arrays from raw bytes through the use of strings or buffers
# 1.6 Use of special library functions

# 2- Array indexing

# 3- Numpy I/O

# 4- Types

# 5- Broadcasting

# 6- Structured Array

# 7- Dispatch

# 8- Subclassing

############
# Praticals
############