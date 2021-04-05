#!/usr/bin/env python3
import numpy as np

# -- Create arrays
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