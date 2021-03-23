#!/usr/bin/env python3

# 'generic import' of math module
import  math

print(math.sqrt(25))


## Basic data types
print("\nBasic data types\n")
print(f"type(2)     : {type(2)}")
print(f"type(2.0)   : {type(2.0)}")
print(f"type('two') : {type('two')}")
print(f"type(True)  : {type(True)}")
print(f"type(None)  : {type(None)}")

print("\nCheck if an object is of a given type\n")
print(f"isinstance(2.0, int)            : {isinstance(2.0, int)}")
print(f"isinstance(2.0, (int, float))   : {isinstance(2.0, (int, float))}")

# convert an object to a given type
print(f"float(2)    : {float(2)}")
print(f"int(2.9)    : {int(2.9)}")
print(f"str(2.9)    : {str(2.9)}")

# zero, None, and empty containers are converted to False
print("\n0, None, and empty containers are converted to False\n")
print(f"bool(0)     : {bool(0)}")
print(f"bool(None)  : {bool(None)}")
print(f"bool('')    : {bool('')}")
print(f"bool([])    : {bool([])}")
print("bool({})    :", f"{bool({})}")

print("\nnon-empty containers and non-zeros are converted to True\n")
print(f"bool(2)     : {bool(2)}")
print(f"bool('two') : {bool('two')}")
print(f"bool([2])   : {bool([2])}")

### Math
# basic operations
print("\nBasic arithmetic operations:\n")
print(f"10 + 4      = {10 + 4}")
print(f"10 - 4      = {10 - 4}")
print(f"10 * 4      = {10 * 4}")
print(f"10 ** 4     = {10 ** 4}")
print(f"10 / 4      = {10 / 4}")
print(f"10/float(4) = {10 / float(4)}")
print(f"5 % 4       = {10 % 4}")
print(f"10 / 4      = {10 / 4}  (true division)")
print(f"10 // 4     = {10 // 4} (floor division)")

## Comparisons and boolean operations
print("\nComparisons and boolean operations:\n")
print("** Comparisons **")
print(f"5 > 3   => {5 > 3}")
print(f"5 >= 3  => {5 >= 3}")
print(f"5 != 3  => {5 != 3}")
print(f"5 == 3  => {5 == 5}")
print("** Boolean operations **")
print(f"(5 > 3) and (6 > 3)             => {(5 > 3) and (6 > 3)}")
print(f"(5 > 3) or (5 < 3)              => {(5 > 3) or (5 < 3)}")
print(f"not False                       => {not False}")
print(f"False or not False and True     => {False or not False and True}")


## Conditional statements
print(f"\nConditional statements:\n")
x = 3
if x > 0:
    print("positive")

#
if x > 0:
    print('positive')
else:
    print('zero or negative')

# if/elif/else
if x > 0:
    print('positive')
elif x == 0:
    print("zero")
else:
    print('negative')

# single-line if statement
if x > 0: print('positive')

# single-line if/else statement, a.k.a tenary operator
print('positive') if x > 0 else print('zero or negative')
