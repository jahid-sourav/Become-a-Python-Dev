# Single line comment

print("I'm Jahid", end=" ")
print("I am a Python Programmer.")
print("I love coding")

'''
long_variable_name = 10
print(long_variable_name)      
Multi-line comment 
'''

number = 7
print("The number is", number)

'''
Python's built-in Data Types:
-----------------------------
01. Numeric Types
------------------
These types are used to represent numbers.
A. int: Integers (e.g., 5, -100).
B. float: Floating-point numbers (e.g., 3.14, -0.5).
C. complex: Complex numbers (e.g., 1 + 2j).

02. Sequence Types
------------------
These types represent ordered collections of items.
A. str: Strings (a sequence of characters). It's immutable.
B. list: Lists (an ordered, mutable collection).
C. tuple: Tuples (an ordered, immutable collection).
D. range: A sequence of numbers often used for looping. It's immutable.

03. Mapping Type
----------------
This type is a collection of key-value pairs.
A. dict: Dictionaries (an unordered, mutable collection of key-value pairs).

04. Set Types
-------------
These types are unordered collections of unique items.
A. set: Sets (a mutable collection).
B. frozenset: Frozen sets (an immutable collection).

05. Boolean Type
----------------
This type represents logical values.
A. bool: Booleans (either True or False).

06. Binary Types
------------
These types handle binary data.
A. bytes: An immutable sequence of bytes.
B. bytearray: A mutable sequence of bytes.
C. memoryview: Provides an efficient way to access the memory of another binary object without copying it.

07. None Type
This type represents the absence of a value.
A. NoneType: The single object of this type is None.

08. Custom Types: User-defined classes (if applicable)
'''

print("The Data Type of",number, "is", type(number))

user_input = input("Please enter your favorite programming language: ")
print("You entered:", user_input)
