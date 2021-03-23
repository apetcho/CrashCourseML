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

#######################
# List data structure
#######################
# create an empty list
empty_list = []         # 1st-way
empty_list = list()     # 2nd-way

# create a list
simpsons = ["homer", "marge", "bart"]
print(f"simpsons        = f{simpsons}")
# examine a list
print(f"simpsons[0]     = {simpsons[0]}")
print(f"len(simpsons)   = {len(simpsons)}")
# modify a list
simpsons.append('lisa')
print(f"simpsons.append('lisa')     => {simpsons}")
simpsons.extend(['itchy', 'scratchy'])
print(f"simpsons.extend(['itchy', 'scratchy'])  => {simpsons}")
simpsons.insert(0, 'maggie')
print(f"simpsons.insert(0, 'maggie')    => {simpsons}")
simpsons.remove('bart')
print(f"simpsons.remove('bart')     => {simpsons}")
simpsons.pop(0)
print(f"simpsons.pop(0)     => {simpsons}")
del simpsons[0]
print(f"del simpsons[0]     => {simpsons}")
simpsons[0] = 'krusty'
print(f"simpsons[0] = 'krusty'      => {simpsons}")

# List slicing [start:end:stride]
weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']
print(f"weekdays        = {weekdays}")
print(f"weekdays[0]     = {weekdays[0]}")
print(f"weekdays[0:3]   = {weekdays[0:3]}")
print(f"weekdays[:3]    = {weekdays[:3]}")
print(f"weekdays[3:]    = {weekdays[3:]}")
print(f"weekdays[-1]    = {weekdays[-1]}")
print(f"weekdays[::2]   = {weekdays[::2]}")
print(f"weekdays[::-1]  = {weekdays[::-1]}")
print("or equivently")
print(f"list(reversed(weekdays))  => {list(reversed(weekdays))}")
print("sort a list inplace")
simpsons.sort()
print(f"simpsons.sort()     => {simpsons}")
simpsons.sort(reverse=True)
print(f"simpsons.sort(reverse=True)     => {simpsons}")
simpsons.sort(key=len)
print(f"Sort by a key: simpsons.sort(key=len)   => {simpsons}")
print("return a sorted list")
print(f"sorted(simpsons) => {sorted(simpsons)}")
print(f"sorted(simpsons, reverse=true)  => {sorted(simpsons, reverse=True)}")
print(f"sorted(simpsons, key=len)       => {sorted(simpsons, key=len)}")

# create a second reference to the same list
print("Create a second reference to the same list")
num = [1, 2, 3]
print(f"num = {num}")
same_num = num
print(f"same_num = num => {same_num}")
same_num[0] = 0
print("same_num[0] = 0")
print(f"    => {same_num}")
print(f"    => {num}")
# copy a list
new_num = num.copy()
new_num = num[:]
new_num = list(num)
print("new_num = num.copy()")
print(f"new_num = {new_num}")
print(f"id(num) == id(same_num)     => {id(num) == id(same_num)}")
print(f"id(num) == id(new_num)      => {id(num) == id(new_num)}")
print(f"num is same_num             => {num is same_num}")
print(f"num is new_num              => {num is new_num}")
print(f"num == same_num             => {num == same_num}")
print(f"num == new_num              => {num == same_num}")
print("Concatenate (+):")
print(f"[1, 2, 3] + [4, 5, 6]       => {[1, 2, 3] + [4, 5, 6]}")
print("Replicate (*):")
print(f"['a']*2 + ['b']*3           => {['a']*2 + ['b']*3}")
