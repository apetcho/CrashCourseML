#!/usr/bin/env python3
import numpy as np

## -- Create arrays
data1 = [1, 2, 3, 4, 5]                 # list
arr1 = np.array(data1)                  # 1d array
data2 = [range(1, 5), range(5, 9)]      # list of lists
arr2 = np.array(data2)                  # 2d array
print(f"data1 = {data1}")
print(f" arr1 = {arr1}")
print(f"data2 = {data2}")
print(f" arr2 = {arr2}")
arr2list = arr2.tolist()                 # convert array back to list
print(f"arr2.tolist() = {arr2list}")

## -- Create special arrays
print(f"np.zeros(10):\n{np.zeros(10)}")
print(f"np.zeros((3, 6)):\n{np.zeros((3, 6))}")
print(f"np.ones(10):\n{np.ones(10)}")
# 0 to 1 (inclusive) with 5 points
print(f"np.linspace(0, 1, 5):\n{np.linspace(0, 1, 5)}")
# 10^0 to 10^3 (inclusive) with 4 points
print(f"np.logspace(0, 3, 4):\n{np.logspace(0, 3, 4)}")

## -- arange
int_array = np.arange(5)
float_array = int_array.astype(float)
print(f"int_array = {int_array}")
print(f"float_array = {float_array}")

## -- Examining arrays
print(f"arr1.dtype = {arr1.dtype}")
print(f"arr2.dtype = {arr2.dtype}")
print(f" arr2.ndim = {arr2.ndim}")
print(f"arr2.shape = {arr2.shape}")
print(f" arr2.size = {arr2.size}")
print(f" len(arr2) = {len(arr2)}")

## -- Reshaping
arr = np.arange(10, dtype=float).reshape((2, 5))
print(f"arr = {arr}")
print(f"arr.shape = {arr.shape}")
print(f"arr.reshape(5, 2) = {arr.reshape((5, 2))}")
a = np.array([0, 1])
a_col = a[: np.newaxis]
print(f"a = {a}\na_col = a[: np.newaxis] = {a_col}")
a_col = a[:, None]
print(f"a = {a}\na_col = a[:, None] = {a_col}")
# Transpose
print("Transpose")
print(f"a_col.T = {a_col.T}")
# Flatten: always returns a flat copy of the original array
print("\n-------------------------------------------\n")
print("np.array.flatten()")
arr_flt = arr.flatten()
arr_flt[0] = 33
print(f"arr:\n{arr}")
print(f"arr_flt:\n{arr_flt}")

# Ravel: returns a view of the original array whenever possible
print("np.array.ravel()")
print(f"arr:\n{arr}")
arr_flt = arr.ravel()
arr_flt[0] = 33
print(f"arr_flt:\n{arr_flt}")
print(f"arr:\n{arr}")

## Stack arrays
# Stack flat arrays in columns
a = np.array([0, 1])
b = np.array([2, 3])
ab =  np.stack((a, b)).T
print(f"a = {a}")
print(f"b = {b}")
print(f"ab = np.stack((a, b)).T = {ab}")
print(f"or\nab = np.hstack((a[:, None], b[:, None])) = {np.hstack((a[:, None], b[:, None]))}")