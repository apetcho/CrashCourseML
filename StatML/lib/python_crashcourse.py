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