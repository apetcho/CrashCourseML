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


########
# Sets
########
empty_set = set()
print(f"empty_set       => {empty_set}")
languages = {'python', 'r', 'java'}
snakes = set(['cobra', 'viper', 'python'])
print(f"languages       => {languages}")
print(f"snakes          => {snakes}")
print(f"len(languages)  => {len(languages)}")
print(f"'python' in languages   => {'python' in languages}")
# Set operations
print(f"languages & snakes      => {languages & snakes}")
print(f"languages | snakes      => {languages | snakes}")
print(f"languages - snakes      => {languages - snakes}")
print(f"snakes - languages      => {snakes - languages}")
languages.add('sql')
languages.add('r')
languages.remove('java')
print(f"languages = {languages}")

try:
    languages.remove('c')
except KeyError as err:
    print(f"Error: {err}")

languages.discard('c')
print(f"languages = {languages}")
languages.pop()
print(f"languages = {languages}")
languages.clear()
print(f"languages = {languages}")
languages.update(['go', 'spark'])
print(f"languages = {languages}")
print(f"sorted(set([9, 0, 2, 1, 0]))    => {sorted(set([9, 0, 2, 1, 0]))}")

###########################################################################
# Functions: This part is based on the official python tutorial (python3.7)
# https://docs.python.org/3.7/tutorial/controlflow.html#defining-functions
############################################################################
print("\n\nFunctions\n")
# Defining functions

def fib(n):
    """
    Print a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)
f = fib
f(100)

###

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result

f100 = fib2(100)
print(f100)


# Default Arguments Values

def ask_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
# _ = ask_ok("Do you really want to quit? ")
# _ = ask_ok("OK to overwrite the file? ", 2)
# _ = ask_ok("OK to overwrite the file?", 2, "Come on, only yes or no!")


# Keywords Arguments

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action="VOOOOM")
parrot(action='VOOOOM', voltage=1000000)
parrot('a million', 'bereft of life', 'jump')
parrot("a thousand", state='pushing up the daisies')


def cheeseshop(kind, *args, **kwargs):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print("-"*40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
           
           
# Arbitrary Argument Lists a.k.a variadics

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

# Unpacking Arguments List
planets = ("earth", "mars", "venus")
d = {"voltage": "four million", "state": "bleedin'demised", "action": "VOOM"}
print(concat(*planets))
parrot(**d)

# Lambda Expression

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
print(f"pairs = {pairs}")
pairs.sort(key=lambda pair: pair[1])    # sort by the 2nd component of pair
print(f"pairs = {pairs}")


# Function Annotations

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return f"{ham} and {eggs}"

print(f('spam'))

###############
# Loops
###############
words = ['cat', 'window', 'defenestrate']
print(f"words = {words}")
# XXX: Dangerorus. The iterable is list, thus mutable.
# If words is being modified in the loop body, infinite copy will be made,
# leading to computation time cost.
for word in words:
    print(word, len(word))

# XXX Best alternative: word with a slice of the entire list
for word in words[:]:
    if len(word) > 6:
        words.insert(0, word)
print(f"words = {words}")

# break and else statements in for loop
for n in range(2, 10):
    for x in range(2, n):
        if n % n == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# continue statement in for loop
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an [even] number", num)
        continue
    print("Found an [odd] number", num)
    
######################
# List Comprehension
######################
squares = []
for x in range(10):
    squares.append(x**2)
print(f"squares = {squares}")

# or
squares = list(map(lambda x: x**2, range(10)))
print(f"squares = {squares}")
# or
squares = [x**2 for x in range(10)]
print(f"squares = {squares}")
# Dictionary comprehension
d = {x: x**2 for x in (2, 4, 6)}
print(f"d = {d}")
# Set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(f"a = {a}")


#####################################
# Object Oriented Programming (OOP)
#####################################
print("\n\n-- INTRODUCTION TO OOP --\n")
# Scopes and Namespaces
print("Scopes and Namespaces:")
def scope_test():
    def do_local():
        spam = "local spam"
        
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        
    def do_global():
        global spam
        spam = "global spam"
        
    spam = "test spam"
    do_local()
    print("After local assignement:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
    
scope_test()
print("In global scope:", spam)

# A First Look at Classes
class MyClass:
    """A simple example class"""
    i = 12345
    
    def f(self):
        return "hello class world"
    
x = MyClass()
print(x.f())

class Complex:
    
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
x = Complex(3.0, -4.5)
print(x.r, x.i)

# Class and Instance Variables

class Dog:
    
    kind = 'canine'         # class variable
    # tricks = []             # mistaken use of class variable
    
    def __init__(self, name):
        self.name = name    # instance variable
        self.tricks = []
        
    def add_trick(self, trick):
        self.tricks.append(trick)
        
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

# Private Variables

class Mapping:
    
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
            
    __update = update       # private copy of original update() method
    

class MappingSubclass(Mapping):
    
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            
            
# Iterators

class Reverse:
    """Iterator for looping over a sequence backwards."""
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
    
print("spam")
rev = Reverse("spam")
print(iter(rev))
for c in rev:
    print(c, end='')


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
data = "golf"
print(data)
for c in reverse(data):
    print(c, end='')
    
# Generator Expressions
print()
x = sum(i*i for i in range(10))
print(x)

xvec = [10, 20, 30]
yvec = [7, 5, 3]

xy = sum(x*y for x, y in zip(xvec, yvec))
print(xy)


#---------------------
print("\n-- END OF OOP ---\n")
######################
# Exceptions handling
######################

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid numbe. Try again...")

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
        
try:
    raise Exception("spam", "eggs")
except Exception as err:
    print(type(err))
    print(err.args)
    print(err)
    
    x, y = err.args
    print(f"x = {x}")
    print(f"y = {y}")
    
def this_fails():
    x = 1/0
    
try:
    this_fails()
except ZeroDivisionError as err:
    print(f"Handling run-time error: {err}")
    
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.
    
    Attributes:
        expression  -- input expression in which the error occured
        message -- explanation of the error
    """
    
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
        
class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.
    
    Attributes:
        previous -- state at the beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed.
    """
    
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
        
divide(2, 1)
divide(2, 0)
# divide("2", "1")
    
#####################################
# Basic Operating system interfaces
#####################################


#############
# Practicals
#############
# Exercise 1: -- functions --

# Exercise 2: -- functions + list + loop --

# Exercise 3: -- File I/O --

# Exerices 4: -- OOP --


