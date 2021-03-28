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
  

nparray_creation_with_intrinsic_1d()

## 2D arrays
## ndarrays

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