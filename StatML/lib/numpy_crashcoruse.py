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
