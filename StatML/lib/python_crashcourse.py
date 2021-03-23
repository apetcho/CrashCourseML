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


##########
# Tuples
##########
print("\n\nTuple data type:\n")
digits = (0, 1, 'two')
digits = tuple([0, 1, 'two'])
zero = (0,)
print(f"digits = (0, 1, 'two')      => {digits}")
print(f"digits[2]                   => {digits[2]}")
print(f"len(digits)                 => {len(digits)}")
print(f"digits.count(0)             => {digits.count(0)}")
print(f"digits.index(1)             => {digits.index(1)}")

# concatenate tuples
digits = digits + (3, 4)
print(f"digits = digits + (3, 4)    => {digits}")
print(f"(3, 4) * 2                  => {(3, 4) * 2}")

#########
# String
#########
# Create a string
s = str(42)
print(f"s = str(42)         => {s}")
s = "I like you"
print(f"s = 'I like you'    => {s}")
print(f"s[0]                => {s[0]}")
print(f"len(s)              => {len(s)}")
print(f"s[:6]               => {s[:6]}")
print(f"s[7:]               => {s[7:]}")
print(f"s[-1]               => {s[-1]}")
print("Basic string methods:\n")
print(f"s.lower()           => {s.lower()}")
print(f"s.upper()           => {s.upper()}")
print(f"s.startswith('I')   => {s.startswith('I')}")
print(f"s.endswith('you')   => {s.endswith('you')}")
print(f"s.isdigit()         => {s.isdigit()}")
print(f"s.find('like')      => {s.find('like')}")
print(f"s.find('hate')      => {s.find('hate')}")
_ = s.replace('like', 'love')
print(f"s.replace('like', 'love')   => {s.replace('like', 'love')}")
print(f"s.split(' ')        => {s.split(' ')}")
print(f"s.split()           => {s.split()}")
s2 = "a, an, the"
print(f"s2 = {s2}")
print(f"s2.split(',')       => {s2.split(',')}")

stooges = ['larry', 'curly', 'moe']
print(f"stooges = {stooges}")
print(f"' '.join(stooges)   => {' '.join(stooges)}")

# Concatenate strings
print("Concatenate strings")
s3 = "The meaning of life is"
s4 = '42'
print(f"s3 = {s3}\ns4 = {s4}")
s5 = ' ham and cheese'
print(f"s5 = {s5}, len = {len(s5)}")
print(f"s5.strip() = {s5.strip()}, len = {len(s5)}")
print("\nString substitutions:\n")
print(f"'raining %s and %s' % ('cats', 'dogs') => {'raining %s and %s' %('cats', 'dogs')}" )
print(r"'raining {} and {}'.format('cats, 'dogs')   => ",
    "raining {} and {}".format('cats', 'dogs'))
print(r"'raining {arg1} and {arg2}'.format(arg1='cats', arg2='dogs')    => ",
    "raining {arg1} and {arg2}".format(arg1='cats', arg2='dogs'))

print(r"'pi is {:.2f}'.format(3.14159) => ",
    "pi is {:.2f}".format(3.14159))
print('first line\nsecond line')
print(r"first line\nfirst line")

#################
# Dictionaries
#################
print("\nDictionaries:\n")
empty_dict = {}
# or
empty_dict = dict()
print(f"empty_dict =>   {empty_dict}")
# Create a dictionary
family = {"dad": "homer", "mom": "marge", "size": 6}
# of
family = dict(dad='homer', mom='marge', size=6)
print(f"family              => {family}")

# Convert a list of tuples into a dictionary
list_of_tuples = [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
family = dict(list_of_tuples)
print(f"list_of_tuples      => {list_of_tuples}")
print(f"family              => {family}")
print(f"family['dad']       => {family['dad']}")
print(f"len(family)         => {len(family)}")
print(f"family.keys()       => {family.keys()}")
print(f"family.values()     => {family.values()}")
print(f"family.items()      => {family.items()}")
print(f"'mom' in family     => {'mom' in family}")
print(f"'marge' in family   => {'marge' in family}")
family['cat'] =  'snowball'
print(f"family['cat'] =  'snowball'     => {family}")
family['cat'] =  'snowball ii'
print(f"family['cat'] =  'snowball ii'  => {family}")
del family['cat']
print(f"del family['cat']           => {family}")
family['kids'] = ['bart', 'lisa']
print(f"family['kids'] = ['bart', 'lisa']   => {family}")
_ = family.pop('dad')
print(f"_ = family.pop('dad')       => {family}")

family.update({"baby": 'maggie', 'grandpa': 'abe'})
print(r"family.update({'baby': 'maggie', 'grandpa': 'abe'})     =>", f" {family}")
print(f"family['mom']               => {family['mom']}\nor\n")
print(f"family.get('mom')           => {family.get('mom')}")
try:
    print(f"family['grandma']       => {family['grandma']}")
except KeyError as err:
    print(f"Error: {err}")

print(f"family.get('grandma')       => {family.get('grandma')}")
print(f"family.get('grandma', 'not found')      => {family.get('grandma', 'not found')}")
print(f"family['kids'][0]           => {family['kids'][0]}")
family['kids'].remove('lisa')
print(f"family['kids'].remove('lisa')   => {family}")
print(r"'youngest child is %(baby)s' % family",
    "youngest child is %(baby)s" % family)

