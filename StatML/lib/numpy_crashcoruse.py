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

## -- Selection
section = lambda n, txt: print(f"{'*'*n}\n{txt}\n{'*'*n}")
section(len("Selection"), "Selection")

arr = np.arange(10, dtype=float).reshape((2, 5))
print(f"arr:\n{arr}")
print(f"arr[0] => {arr[0]}")
print(f"arr[0, 3] => {arr[0, 3]}")
print(f"arr[0][3] => {arr[0][3]}")

# Slicing
txt = "Slicing"
section(len(txt), txt)
print(f"arr[0, :] => {arr[0, :]}")
print(f"arr[:, 0] => {arr[:, 0]}")
print(f"arr[:, :2] => {arr[:, :2]}")
print(f"arr[:, 2:] => {arr[:, 2:]}")
arr2 = arr[:, 1:4]
print(f"arr2 = arr[:, 1:4] =>\n{arr2}")
print(f"arr =>\n{arr}")
arr2[0, 0] = 33
print(f"After arr2[0, 0] = 33")
print(f"arr2 =>\n{arr2}")
print(f"arr =>\n{arr}")
print(f"Row 0: {arr[0, :]}")
print(f"Row 0 in reverse order: {arr[0, ::-1]}")

# -- Fancy indexing: Integer or bollean array indexing
txt = "Fancy indexing: Integer or bollean array indexing"
section(len(txt), txt)
arr2 = arr[:, [1, 2, 3]]
print(f"arr =>\n{arr}")
print("\narr2 = arr[:, [1, 2, 3]]\n")
print(f"arr2 =>\n{arr2}")
arr2[0, 0] = 44
print("After arr2[0,0] = 44")
print(f"arr2 =>\n{arr2}\narr =>\n{arr}")

print("\nBoolean arrays indexing\n")
arr2 = arr[arr > 5]
print(f"arr2 =>{arr2}")
arr2[0] = 44
print(f"arr2 = {arr2}")
print(f"arr =>\n{arr}")

arr[arr > 5] = 0
print("After arr[arr > 5] = 0")
print(f"arr =>\n{arr}")

#
names = np.array(["Bob", "Joe", "Will", "Bob"])
print(f"names = {names}")
print(f"names == 'Bob' => {names == 'Bob'}")
print(f"names[names != 'Bob'] => {names[names != 'Bob']}")
print("(names == 'Bob') | (names == 'Will') => ")
print(f"{(names == 'Bob') | (names == 'Will')}")
print("names[names != 'Bob'] = 'Joe' =>")
names[names != 'Bob'] = 'Joe'
print(f"{names}")
print("np.unique(names)")
print(f"{np.unique(names)}")

## - Vectorized operations
txt = "Vectorized operations"
section(len(txt), txt)

nums = np.arange(5)
print(f"nums = {nums}")
print(f"nums * 10 => {nums * 10}")
nums = np.sqrt(nums)
print(f"nums = np.sqrt(nums) => {nums}")
print(f"np.ceil(nums) => {np.ceil(nums)}")
print(f"np.isnan(nums) => {np.isnan(nums)}")
print(f"nums + np.arange(5) => {nums + np.arange(5)}")
print(f"np.maximum(nums, np.array([1, -1, 3, -4, 5])) => {np.maximum(nums, np.array([1, -2, 3, -4, 5]))}")

# Compute Euclidian distance between 2 vectors
vec1 = np.random.randn(10)
vec2 = np.random.randn(10)
dist = np.sqrt(np.sum((vec1 - vec2)**2))
print(f"vec1 = {vec1}")
print(f"vec2 = {vec2}")
print(f"dist = {dist}")

# math and stats
rnd = np.random.randn(4, 2)
print(f"rnd:\n{rnd}")
print(f"rnd.mean()      => {rnd.mean()}")
print(f"rnd.std()       => {rnd.std()}")
print(f"rnd.argmin()    => {rnd.argmin()}")
print(f"rnd.sum()       => {rnd.sum()}")
print(f"rnd.sum(axis=0) => {rnd.sum(axis=0)}")
print(f"rnd.sum(axis=1) => {rnd.sum(axis=1)}")

# methods for boolean arrays
print(f"(rnd > 0).sum() => {(rnd > 0).sum()}")
print(f"(rnd > 0).any() => {(rnd > 0).any()}")
print(f"(rnd > 0).all() => {(rnd > 0).all()}")

# random numbers
np.random.seed(12234)
print(f"np.random.rand(2, 3):\n{np.random.rand(2, 3)}")
print(f"np.random.randn(10):\n{np.random.randn(10)}")
print(f"np.random.randint(0, 2, 10):\n{np.random.randint(0, 2, 10)}")
