import re
# Class: 01

# Single Comment 

'''
Multi-line Comment
This is a multi-line comment.
'''

print("Hello, World!", end=" ")
print("I'm learning Python.")

number = 7
print("The number is:", number)

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

print("The Data Type of Number is:", type(number))

user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

user_age = int(input("Enter your age: "))
print("You are " + str(user_age) + " years old.")

# Class: 02
# Python Operators and If-Else Statements

'''
Arithmetic Operators
+ = Addition
- = Subtraction
* = Multiplication
/ = Division
% = Modulus
** = Exponentiation
// = Floor Division
'''

'''
Assignment Operators
= : Simple assignment
+= : Add and assign
-= : Subtract and assign
*= : Multiply and assign
/= : Divide and assign
%= : Modulus and assign
**= : Exponentiation and assign
//= : Floor division and assign

&= : Bitwise AND and assign
|= : Bitwise OR and assign
^= : Bitwise XOR and assign
>>= : Bitwise right shift and assign
<<= : Bitwise left shift and assign
'''

'''
Comparison Operators
== : Equal to
!= : Not equal to
> : Greater than
< : Less than
>= : Greater than or equal to
<= : Less than or equal to
'''

'''
Logical Operators
and : Logical AND
or : Logical OR
not : Logical NOT
'''

'''
Bitwise Operators
& : Bitwise AND
| : Bitwise OR
^ : Bitwise XOR
~ : Bitwise NOT
<< : Bitwise left shift
>> : Bitwise right shift
'''

'''
Membership Operators
--------------------
এই অপারেটরগুলো কোনো ডেটা বা ভ্যালুকোনো সিকোয়েন্সের 
(যেমন: স্ট্রিং, লিস্ট, টাপল) মধ্যে আছে কি না তা পরীক্ষা করে।

in : Returns True if a value is found in the specified sequence
Example: 'a' in 'apple' returns True

not in : Returns True if a value is not found in the specified sequence
Example: 'b' not in 'apple' returns True
'''

'''
Indentity Operators
--------------------
এই অপারেটরগুলো দুইটি ভ্যারিয়েবল একই অবজেক্টকে রেফার করছে কি না তা পরীক্ষা করে।

is : Returns True if both variables point to the same object
Example: 
x = [1, 2], y = [1, 2], x is y 
returns False

is not : Returns True if both variables do not point to the same object
Example:
x = [1, 2], y = [1, 2], x is not y
returns True
'''

# Problem Solving with If-Else Statements

# Program to check if a person is eligible to vote based on age
try:
    user_age = int(input("Enter Your Age: "))
    user_nationality = int(input("Enter Your Nationality(1 for Bangladeshi, 0 for Foreigner): "))


    if user_age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    elif user_age >= 18 and user_nationality == 1:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

except ValueError:
    print("Invalid input. Please enter a valid age and nationality.")

# Program to determine the grade based on marks
try:
    user_marks = int(input("\nEnter Your Marks: "))

    if user_marks < 0 or user_marks > 100:
        print("Invalid Marks")

    else:
        if user_marks >= 80:
            print("You got A+")     

        elif user_marks >= 70:
            print("You got A")

        elif user_marks >= 60:
            print("You got A-")

        elif user_marks >= 50:
            print("You got B")

        elif user_marks >= 40:
            print("You got C")

        elif user_marks >= 33:
            print("You got D")

        elif user_marks < 33:
            print("You got F")

except ValueError:
    print("Invalid input. Please enter numeric marks.")

# Even or Odd Number Check
try:
    user_number = int(input("\nEnter a number to check if it is even or odd: "))
    if user_number < 0:
        print("Please enter a non-negative integer.")
    else:
        if user_number % 2 == 0:
            print("The number is even.")            
        else:
            print("The number is odd.")

except ValueError:
    print("Invalid input. Please enter an integer.")

# Find the largest of three numbers
try:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))


    if num1 < 0 or num2 < 0 or num3 < 0:
        print("Please enter non-negative numbers.")
    else:
        if num1 >= num2 and num1 >= num3:
            largest = num1
        elif num2 >= num1 and num2 >= num3:
            largest = num2
        else:
            largest = num3

    print(f"The largest number is: {largest}")

except ValueError:
    print("Invalid input. Please enter numeric values.")

# Leap Year
try:
    user_input = int(input("\nEnter a year: "))
    if user_input < 0:
        print("Please enter a valid positive year.")
    else:
        if((user_input % 4 == 0 and user_input % 100 != 0) or (user_input % 400 == 0)):
            print(f"{user_input} is a leap year.")
        else:
            print(f"{user_input} is not a leap year.")

except ValueError:
    print("Invalid input. Please enter a valid year.")

# Vowel or Consonant
try:
    given_char = input("\nEnter a character: ").lower()

    if len(given_char) == 1 and given_char.isalpha():   
        if given_char in 'aeiou':
            print(f"{given_char} is a vowel.")
        else:
            print(f"{given_char} is a consonant.")

    else:
        print("Invalid input. Please enter a single alphabet character.")

except Exception as e:
    print("An error occurred:", e)


# Class: 03
# Loops in Python

'''
There are two primary types of loops in Python:
1. For Loop
2. While Loop

For Loop Structure:
for variable in sequence:
    # code block to be executed 

While Loop Structure:
while condition:
    # code block to be executed

Example of For Loop:
for i in range(5):
    print(i)
Answer: 0 1 2 3 4

for i in range(1, 6, 2):
    print(i)
Answer: 1 3 5 
Explanation: Starts at 1, ends before 6, increments by 2

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
Answer: apple banana cherry

Example of While Loop:
i = 0
while i < 5:
    print(i)
    i += 1
Answer: 0 1 2 3 4

password = ""
while password != "secret":     
    password = input("Enter the password: ")
print("Access Granted")

Break and Continue Statements:
- break: Exits the loop immediately.(একে বারে লুপ থামিয়ে দেয়)
- continue: Skips the current iteration and moves to the next one.(লুপের নির্দিষ্ট অংশ বাদ দিয়ে পরের অংশে চলে যায়)

Example of Break and Continue:
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
Answer: 0 1 2 3 4

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
Answer: 1 3 5 7 9
'''

# Sum
try:
    give_number = int(input("Enter a number: "))
    total = 0
    for i in range(1, give_number + 1):
        total += i
    print(f"The sum of all numbers from 1 to {give_number} is: {total}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")


# Multiplication Table
try:
    user_input = int(input("Enter A Number: "))
    for i in range(1, 11):
        print(f"{user_input} x {i} = {user_input * i}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")

# Factorial
try:  
    factorial_number = int(input("Enter a number to calculate its factorial: "))
    factorial_result = 1
    while factorial_number > 1:
        factorial_result *= factorial_number
        factorial_number -= 1
    print(f"The factorial is: {factorial_result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")

''' 
---------------------
Conditional Statement
---------------------
Largest among Three Numbers: 
Write a Python program that takes three numbers as input and prints out the largest among them.
'''
try:
    input_one = int(input("Enter The First Number: "))
    input_two = int(input("Enter The Second Number: "))
    input_three = int(input("Enter The Third Number: "))

    if input_one >= input_two and input_one >= input_three:
        largest = input_one
    elif input_two >= input_one and input_two >= input_three:
        largest = input_two
    else:
        largest = input_three

    print(f"The Largest Number is: {largest}")

except ValueError:
    print("Please enter valid integer numbers.")


'''
Conditional Statement
---------------------
Quadrant Identifier: 
Write a Python program that takes the coordinates (x, y) of a point as input and prints out which quadrant it belongs to (1st, 2nd, 3rd, or 4th).
'''
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("The point is in the 1st Quadrant (Q1).")
elif x < 0 and y > 0:
    print("The point is in the 2nd Quadrant (Q2).")
elif x < 0 and y < 0:
    print("The point is in the 3rd Quadrant (Q3).")
elif x > 0 and y < 0:
    print("The point is in the 4th Quadrant (Q4).")
elif x == 0 and y == 0:
    print("The point is at the Origin.")
elif x == 0:
    print("The point lies on the Y-axis.")
elif y == 0:
    print("The point lies on the X-axis.")


'''
Conditional Statement
---------------------
Age Classifier: 
Write a Python program that takes a person's age as input and prints out whether they are an infant (0-1), toddler (2-3), child (4-12), teenager (13-19), adult (20+).
'''
try:
    age = int(input("Enter the person's age: "))
    if age < 0:
        print("Age cannot be negative.")
    elif age <= 1:
        print("The person is an infant.")
    elif age <= 3:
        print("The person is a toddler.")       
    elif age <= 12:
        print("The person is a child.")
    elif age <= 19:
        print("The person is a teenager.")
    else:
        print("The person is an adult.")

except ValueError:
    print("Please enter a valid integer for age.")


'''
Conditional Statement
---------------------
BMI Calculator: 
Write a Python program that takes a person's height (in meters) and weight (in kilograms) as input and calculates their Body Mass Index (BMI). Print out their BMI and a message indicating whether they are underweight (<18.5), normal (18.5-24.9), overweight (25-29.9), or obese(>=30).
'''
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
try:
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print(f"BMI: {bmi:.2f} - Underweight")
    elif 18.5 <= bmi < 25:
        print(f"BMI: {bmi:.2f} - Normal weight")
    elif 25 <= bmi < 30:
        print(f"BMI: {bmi:.2f} - Overweight")
    else:
        print(f"BMI: {bmi:.2f} - Obese")

except ValueError:
    print("Please enter valid numbers for weight and height.")

'''
Conditional Statement
---------------------
Temperature Converter: 
Write a Python program that takes a temperature input in Celsius and converts it to Fahrenheit if the temperature is above 0°C, or to Kelvin if the temperature is below 0°C.
'''
try:
    celsius = float(input("Enter temperature in Celsius: "))
    if celsius > 0:
        fahrenheit = (celsius * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F") 
    elif celsius < 0:
        kelvin = celsius + 273.15
        print(f"Temperature in Kelvin: {kelvin:.2f}K")  
    else:
        print("Temperature is 0°C, which is neither above nor below zero.")
except ValueError:
    print("Please enter a valid number for temperature in Celsius.")

'''
Conditional Statement
---------------------
Simple Calculator: 
Input two numbers and an operator (+, -, *, /).Use if-elif to perform the operation and print the result. Handle division by zero using conditions.
'''
try:
    numbOne = int(input("Enter first number: "))
    numbTwo = int(input("Enter second number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    if operator == '+':
        result = numbOne + numbTwo
        print(f"The result of {numbOne} + {numbTwo} is: {result}")  
    elif operator == '-':
        result = numbOne - numbTwo
        print(f"The result of {numbOne} - {numbTwo} is: {result}")  
    elif operator == '*':
        result = numbOne * numbTwo
        print(f"The result of {numbOne} * {numbTwo} is: {result}")
    elif operator == '/':
        if numbTwo == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = numbOne / numbTwo
            print(f"The result of {numbOne} / {numbTwo} is: {result}") 
    else:
        print("Invalid operator. Please use +, -, *, or /.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
    

'''
Loops
-----
FizzBuzz: 
Write a Python program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz" using a for loop.
'''
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")   
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)    


'''
Loop
----
Armstrong Number Checker: Write a Python program that takes an integer input from the user and checks if it is an Armstrong number (a number that is equal to the sum of its own digits raised to the power of the number of digits) using a for loop.
'''
try:
    number = int(input("Enter an integer: "))
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        number_str = str(number)
        number_digits = len(number_str)
        total = 0
    
    for digit in number_str:
        total += int(digit) ** number_digits
        if total == number:
            print(f"{number} is an Armstrong number.")
            break
    else:
        print(f"{number} is not an Armstrong number.")  

except ValueError:
    print("Invalid input. Please enter a valid integer.")


'''
Loop
----
Number Reverser: 
Write a Python program that takes an integer input from the user and prints its reverse using a while loop.
'''
try:
    num = int(input("Enter an integer: "))
    reversed_num = 0        
    while num > 0:
        digit = num % 10 
        print("Current Digit:", digit)        
        reversed_num = reversed_num * 10 + digit 
        num = num // 10                        
        print("Reversed Number:", reversed_num)

except ValueError:
    print("Invalid input! Please enter a valid integer.")   


'''
Loop
----
Sum of Digits: 
Write a Python program that takes an integer input from the user and calculates the sum of its digits using a while loop.
'''
try:
    number = int(input("Enter an integer: "))
    total = 0
    original_number = number
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    print(f"The sum of the digits of {original_number} is {total}.")

except ValueError:
    print("Please enter a valid integer.")

'''
Loop
----
Print the pattern (for/while):
1
22
333
4444
55555
'''
for i in range(1, 6):
    print(str(i) * i)
    


'''
Loop
----
Fibonacci Sequence (for loop): 
Input N. Print the first N terms of the Fibonacci sequence.
'''
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer")
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ') 

        temp = a + b  
        a = b         
        b = temp  


'''
Loop
----
Password Retry System (while loop) : 
Predefined password. Let user try until correct or after 3 failed attempts show "Account locked"
'''

password = "abcd1234"
attempts = 0  

while attempts < 3:   
    user_input = input("Enter your password: ")

    if user_input == password:
        print("Access granted")
        break   
    else:
        print("Incorrect password")
        attempts += 1   

if attempts == 3:
    print("Account locked")


'''
Loop
----
Guess the Number Game (while loop): 
Consider a random number between 1 and 10. Let user guess until correct. Give hints:“Too high” or “Too low”.
'''
import random
correct_number = random.randint(1, 10)
while True:
    try:
        guess = int(input('Guess a number between 1 and 10: '))
        if guess < 1 or guess > 10:
            print('Please enter a number between 1 and 10.')
        elif guess > correct_number:
            print('Too high!')
        elif guess < correct_number:
            print('Too low!')    
        else:
            print('Congratulations! You guessed the number!')
            break       
    except ValueError:
        print('Invalid input. Please enter a number between 1 and 10.')


# Class: 04
# Strings, List, Tuple, Dictionary
'''
Strings
-------
Strings are immutable sequences of characters used to store text data. Strings are better for memory optimization because String's Hash value can be cached(example: for the use Dictionary Key).
'''
s1 = "Hello, World!"
s2 = 'Python'
s3 = """This is a multi-line
string."""
s4 = r"C:\Users\Name"  # Raw string to ignore escape sequences
print(s1)
print(s2)
print(s3)
print(s4)

# String Operations and Methods
print("Concatenated string:", s1 + " " + s2) # Concatenation
print("Repetition:", s2 * 3) # Repetition
print("Sliced string (0-5):", s1[0:5:2])  # Slicing(Start:End:Step)
print("Length of s1:", len(s1))  # Length of the string
print("s1 in uppercase:", s1.upper())  # Convert to uppercase
print("s1 in lowercase:", s1.lower())  # Convert to lowercase
print("s1 capitalized:", s1.capitalize()) # Capitalize the first letter
print("s1 capitalized:", s1.title()) # Capitalize the first letter of each word
print("s3 White spaces removed:", s3.strip())  # Remove leading/trailing whitespace
print("s3 Leading Whitespace:", s3.lstrip())  # Remove leading whitespace
print("s3 Trailing Whitespace:", s3.rstrip())  # Remove trailing whitespace

# Sub Stings Search Method
text = "I love Python programming"
print("Python" in text) # এটা দিয়ে সরাসরি চেক করা যায় substring আছে কি না।
print(text.find("Python"))   # substring খুঁজে পেলে প্রথম index return করবে, না পেলে -1 return করবে
print(text.index("Python"))  # find() এর মতোই, কিন্তু substring না পেলে ValueError exception দিবে।
print(text.index("Java"))    # Error → ValueError: substring not found
print(text.rfind("Python"))   
# ডান দিক (Right) থেকে খুঁজবে এবং substring এর index return করবে। না পেলে -1 দিবে।
print(text.find("Python")) # (normal find left থেকে)
print(text.rindex("Python")) # এটাও rfind() এর মতো, কিন্তু substring না পেলে error দিবে।
print(text.startswith("Java")) # False চেক করবে string কি নির্দিষ্ট substring দিয়ে শুরু হয়েছে কিনা।
print(text.endswith("awesome")) # চেক করবে string কি নির্দিষ্ট substring দিয়ে শেষ হয়েছে কিনা।
print(text.count("Python")) # কতবার substring আছে সেটা গুনে দিবে।

text1 = "Python is fun. Python is powerful. I love Python!"
print(re.search("Python", text)) # প্রথম match খুঁজবে
print(re.findall("Python", text))  # ['Python', 'Python', 'Python'] সব match return করবে 

print("s1 replaced 'World' with 'Python':", s1.replace("World", "Python"))  # Replace substring

# Split
words = text.split()
print(words) # ['I', 'love', 'Python', 'programming']

data = "apple,banana,mango,orange"
all_fruit = data.split(",")
print(all_fruit) # ['apple', 'banana', 'mango', 'orange']
print(data.split(" ", 2)) # maxsplit = 2 মানে দুইবার split হবে, তারপর বাকি string একসাথে থাকবে।

demo = "id,name,age,city,country"
print(demo.rsplit(",", 2)) # ['id,name,age', 'city', 'country'] ডান দিক থেকে 2 বার ভাগ করেছে → ফলে শেষের 2 টুকরো আলাদা হয়ে গেছে।

demo_data = """id,name,age
1,Sourav,24
2,Hasan,25
3,Nahid,23"""

rows = data.splitlines()
print(rows) # ['id,name,age', '1,Sourav,24', '2,Hasan,25', '3,Nahid,23'] splitlines() string কে লাইনে ভাগ করে।

lines = ["Line 1", "Line 2", "Line 3"]
text = "\n".join(lines)
print(text)
'''
Line 1
Line 2
Line 3
'''

words = ['I', 'love', 'Python']
sentence = " ".join(words)
print(sentence) # I love Python

print("123".isdigit())  # চেক করে string এর সব character কি শুধুমাত্র digit (0–9)
print("Python".isalpha()) # চেক করে string এর সব character কি alphabetic (a–z বা A–Z)
print("Hello!".isalnum()) # False (! থাকার কারণে) চেক করে সব character কি alphabet বা digit (মানে Alphanumeric)

# String formatting করার একটা পুরোনো এবং powerful system
my_name = "Sourav"
my_age = 24
print("My name is {} and I am {} years old".format(my_name, my_age))
# My name is Sourav and I am 24 years old


# এটা সবচেয়ে modern এবং readable system।
name_a = "Sourav"
age_a = 24
print(f"My name is {name_a} and I am {age_a} years old")
# My name is Sourav and I am 24 years old

# Lists
'''
Python-এ List হলো একটি ordered এবং mutable (পরিবর্তনযোগ্য) collection, যা বিভিন্ন ধরনের element রাখতে পারে।

List এর বৈশিষ্ট্য:

Ordered: element গুলোর একটা নির্দিষ্ট order আছে।

Mutable: element পরিবর্তন করা যায়।

Duplicates allowed: একই value একাধিকবার থাকতে পারে।

Different data types: int, string, float, even other lists থাকতে পারে।
'''
# Empty list
my_list = []

# With elements
numbers_list = [1, 2, 3, 4, 5]
fruits_list = ["apple", "banana", "mango"]
mixed = [1, "apple", 3.5, True]

'''
Accessing Elements (Element Access করা)
List এর element index দ্বারা access করা যায়। Indexing 0 থেকে শুরু হয়।
'''
fruits_1 = ["apple", "banana", "mango"]
print(fruits_1[0])  # apple
print(fruits_1[1])  # banana
print(fruits_1[-1]) # mango (last element)

'''
List Methods (মেথড)
Python list অনেক মেথড প্রদান করে। নিচে সব মেথড উদাহরণসহ দেখানো হলো।
'''

# append() একটি element list এর end এ যোগ করে।
fruits_02 = ["apple", "banana"]
fruits_02.append("mango")
print(fruits_02)  # ['apple', 'banana', 'mango']

# insert() নির্দিষ্ট index এ element insert করে।
fruits_03 = ["apple", "banana"]
fruits_03.insert(1, "mango")  # index 1-এ যোগ করা
print(fruits_03)  # ['apple', 'mango', 'banana']

# extend() একটি list কে অন্য list এর সাথে যোগ করে।
fruits_04 = ["apple", "banana"]
more_fruits = ["mango", "orange"]
fruits_04.extend(more_fruits)
print(fruits_04)  # ['apple', 'banana', 'mango', 'orange']

# remove() প্রথম occurrence of element remove করে।
fruits_05 = ["apple", "banana", "mango", "banana"]
fruits_05.remove("banana")
print(fruits_05)  # ['apple', 'mango', 'banana']

# pop() Index দ্বারা element remove করে এবং return করে। Default last element remove করে।
fruits_06 = ["apple", "banana", "mango"]
popped = fruits_06.pop()
print(popped)  # mango
print(fruits_06)  # ['apple', 'banana']

# specific index
fruits_06.pop(0)
print(fruits_06)  # ['banana']

# clear() List এর সব element remove করে।
fruits_07 = ["apple", "banana"]
fruits_07.clear()
print(fruits_07)  # []

# index() Element এর first occurrence এর index return করে।
fruits_08 = ["apple", "banana", "mango"]
print(fruits_08.index("banana"))  # 1

# count() List এ element কতবার আছে তা return করে।
fruits_09 = ["apple", "banana", "mango", "banana"]
print(fruits_09.count("banana"))  # 2

# sort() List কে ascending order এ sort করে। (Strings ও sort করা যায়)
numbers_10 = [5, 2, 8, 1]
numbers_10.sort()
print(numbers_10)  # [1, 2, 5, 8]

fruits_10 = ["banana", "apple", "mango"]
fruits_10.sort()
print(fruits_10)  # ['apple', 'banana', 'mango']

# reverse() List কে reverse করে।
numbers_11 = [1, 2, 3, 4]
numbers_11.reverse()
print(numbers_11)  # [4, 3, 2, 1]

# copy() List এর copy তৈরি করে।
fruits_11 = ["apple", "banana"]
new_list = fruits_11.copy()
print(new_list)  # ['apple', 'banana']

# len() List এর length return করে (built-in function)
fruits_12 = ["apple", "banana", "mango"]
print(len(fruits_12))  # 3

# slicing List এর একটি অংশ নেওয়া যায়।
numbers_12 = [1, 2, 3, 4, 5]
print(numbers_12[1:4])  # [2, 3, 4]
print(numbers_12[:3])   # [1, 2, 3]
print(numbers_12[2:])   # [3, 4, 5]
print(numbers_12[-3:-1]) # [3, 4]

# in operator Check করা element list এ আছে কিনা।
fruits_13 = ["apple", "banana", "mango"]
print("apple" in fruits_13)  # True
print("orange" in fruits_13) # False

# multiplication List কে repeat করা যায়।
numbers_13 = [1, 2]
print(numbers_13 * 3)  # [1, 2, 1, 2, 1, 2]

# list comprehension List থেকে নতুন list তৈরি করা যায় condition সহ।
numbers_14 = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers_14]
print(squares)  # [1, 4, 9, 16, 25]

# Only even numbers
evens = [x for x in numbers_14 if x % 2 == 0]
print(evens)  # [2, 4]

# List এর সাথে Built-in Functions, এগুলো আলাদা মেথড না, কিন্তু list এর উপর সবচেয়ে বেশি ব্যবহার হয়।
numbers_15 = [10, 20, 30, 40, 50]
print(len(numbers_15))   # 5 → মোট element সংখ্যা
print(min(numbers_15))   # 10 → সবচেয়ে ছোট সংখ্যা
print(max(numbers_15))   # 50 → সবচেয়ে বড় সংখ্যা
print(sum(numbers_15))   # 150 → সব সংখ্যার যোগফল

# Membership Operators (in / not in) 
fruits_14 = ["apple", "banana", "mango"]
print("apple" in fruits_14)   # True
print("orange" not in fruits_14) # True

# Nested Lists (List এর ভিতরে List)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])     # [1, 2, 3]
print(matrix[1][2])  # 6 (row 2, column 3)

# Iterating Over Lists (Loop দিয়ে ঘোরা)
fruits_15 = ["apple", "banana", "mango"]

for fruit in fruits_15:
    print(fruit)

# index সহ
for i, fruit in enumerate(fruits_15):
    print(i, fruit)

# Copying Lists
a = [1, 2, 3]
b = a.copy()      # shallow copy
b[0] = 100

print(a)  # [1, 2, 3]
print(b)  # [100, 2, 3]

# deep copy (nested list এর জন্য)
import copy
nested = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested)
deep_copy[0][0] = 99
print(nested)      # [[1, 2], [3, 4]]
print(deep_copy)   # [[99, 2], [3, 4]]

# List Comprehension (Powerful Shortcut)
numbers_16 = [1, 2, 3, 4, 5]
# square
squares = [x**2 for x in numbers_16]
print(squares)  # [1, 4, 9, 16, 25]

# even numbers
evens = [x for x in numbers_16 if x % 2 == 0]
print(evens)  # [2, 4]

# nested loop
pairs = [(x, y) for x in [1,2] for y in [3,4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# Convert Between Types
# string → list
s = "hello"
print(list(s))  # ['h', 'e', 'l', 'l', 'o']

# tuple → list
t = (1, 2, 3)
print(list(t))  # [1, 2, 3]

# set → list
st = {1, 2, 3}
print(list(st))  # [1, 2, 3]

# Useful Tricks
numbers_17 = [1, 2, 3, 4, 5]

print(numbers_17[::-1])   # reverse [5, 4, 3, 2, 1]
print(numbers_17[::2])    # skip 1 step [1, 3, 5]

# unpacking
i, j, *rest = numbers_17
print(i, j, rest)  # 1 2 [3, 4, 5]

'''
Tuple
------
Tuple হলো ordered collection
Tuple হলো immutable (পরিবর্তন করা যায় না)
Tuple এর মধ্যে different data types রাখা যায়
Tuple এর মধ্যে duplicate values থাকতে পারে
'''
# empty tuple
t1 = ()

# single element (comma দিতে হবে)
t2 = (5,)

# multiple elements
t3 = (1, 2, 3, "apple", 3.5)

print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>

# Tuple Access (Index & Slicing)
fruits_20 = ("apple", "banana", "mango")
print(fruits_20[0])   # apple
print(fruits_20[-1])  # mango
print(fruits_20[1:])  # ('banana', 'mango')

# Tuple Methods Tuple immutable, তাই list এর মতো অনেক মেথড নেই। মোটামুটি 2টা built-in method আছে:
# count()
nums = (1, 2, 2, 3, 2)
print(nums.count(2))  # 3

# index()
nums = (10, 20, 30, 40)
print(nums.index(30))  # 2

# Tuple Operations
# Concatenation
v = (1, 2)
p = (3, 4)
print(v + p)  # (1, 2, 3, 4)

# Repetition
nums_01 = (1, 2)
print(nums_01 * 3)  # (1, 2, 1, 2, 1, 2)

# Membership Test
fruits_90 = ("apple", "banana", "mango")
print("apple" in fruits_90)   # True
print("orange" not in fruits_90)  # True

# Tuple Unpacking
person = ("Sourav", 24, "Bangladesh")
name, age, country = person
print(name)     # Sourav
print(age)      # 24
print(country)  # Bangladesh

# Extended unpacking
nums_20 = (1, 2, 3, 4, 5)
ax, bx, *rest = nums_20
print(ax, bx, rest)   # 1 2 [3, 4, 5]

# Nested Tuple
nested_t = (1, (2, 3), (4, 5))
print(nested_t[1])     # (2, 3)
print(nested_t[1][0])  # 2

# Tuple as Dictionary Key - Tuple immutable, তাই dictionary এর key হিসেবে ব্যবহার করা যায়।
locations = {
    (23.7, 90.4): "Dhaka",
    (22.3, 91.8): "Chattogram"
}
print(locations[(23.7, 90.4)])  # Dhaka

# Built-in Functions with Tuple
nums_02 = (10, 20, 30, 40)
print(len(nums_02))  # 4
print(min(nums_02))  # 10
print(max(nums_02))  # 40
print(sum(nums_02))  # 100

# Advanced Uses
# Tuple in Loops
pairs = [(1, "a"), (2, "b"), (3, "c")]

for num, char in pairs:
    print(num, char)

# Tuple Packing & Returning Multiple Values
def get_info():
    return ("Sourav", 24, "Bangladesh")

info = get_info()
print(info)  # ('Sourav', 24, 'Bangladesh')


# Dictionary
'''
Dictionary হলো unordered, mutable collection of key-value pairs
প্রতিটা item থাকে → key : value আকারে
Key হতে হবে immutable (string, number, tuple ইত্যাদি)
Value হতে পারে যেকোনো data type
'''
# Syntax 
# empty dictionary
d1 = {}
# with values
student = {
    "name": "Sourav",
    "age": 24,
    "country": "Bangladesh"
}
# Access Dictionary Values
print(student["name"])      # Sourav
print(student.get("age"))   # 24
# get() এ key না থাকলে error না দিয়ে None দেয়
print(student.get("grade", "Not Found"))  # Not Found

# Dictionary Methods (with Examples)

# 1. dict.keys() সব key return করে
print(student.keys())  
# dict_keys(['name', 'age', 'country'])

# 2. dict.values() সব value return করে
print(student.values())  
# dict_values(['Sourav', 24, 'Bangladesh'])

# 3. dict.items() সব key-value pair tuple আকারে return করে
print(student.items())  
# dict_items([('name', 'Sourav'), ('age', 24), ('country', 'Bangladesh')])

# 4. dict.update() dictionary তে নতুন key-value যোগ করে বা পুরোনোটা আপডেট করে
student.update({"age": 25, "subject": "CSE"})
print(student)
# {'name': 'Sourav', 'age': 25, 'country': 'Bangladesh', 'subject': 'CSE'}

# 5. dict.pop(key) একটা key remove করে এবং তার value return করে
age = student.pop("age")
print(age)       # 25
print(student)   # {'name': 'Sourav', 'country': 'Bangladesh', 'subject': 'CSE'}

# 6. dict.popitem() শেষের key-value pair remove করে
pair = student.popitem()
print(pair)      # ('subject', 'CSE')
print(student)   # {'name': 'Sourav', 'country': 'Bangladesh'}


# 7. dict.clear() সব elements remove করে
student.clear()
print(student)  # {}

# 8. dict.copy() একটা shallow copy তৈরি করে
person = {"name": "Sourav"}
new_person = person.copy()
new_person["name"] = "Rahim"

print(person)     # {'name': 'Sourav'}
print(new_person) # {'name': 'Rahim'}

# 9.dict.fromkeys() একটা নতুন dict তৈরি করে নির্দিষ্ট keys দিয়ে
keys = ["id", "name", "age"]
new_dict = dict.fromkeys(keys, None)
print(new_dict)  
# {'id': None, 'name': None, 'age': None}

# 10. dict.setdefault(key, default) যদি key না থাকে তাহলে default value সেট করে দেয়
student = {"name": "Sourav"}
student.setdefault("age", 24)
print(student)  # {'name': 'Sourav', 'age': 24}

# Iterating Over Dictionary
student = {"name": "Sourav", "age": 24, "country": "Bangladesh"}

# keys
for k in student.keys():
    print(k)

# values
for v in student.values():
    print(v)

# items
for k, v in student.items():
    print(f"{k} → {v}")


# Nested Dictionary
students = {
    "101": {"name": "Sourav", "age": 24},
    "102": {"name": "Rahim", "age": 22}
}

print(students["101"]["name"])  # Sourav


# Dictionary Comprehension
# square dictionary
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# filter dictionary
evens = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print(evens)  # {2: 4, 4: 16}

# Built-in Functions with Dictionary
student = {"name": "Sourav", "age": 24, "country": "Bangladesh"}
print(len(student))     # 3
print("name" in student)  # True
print("grade" not in student)  # True

# Dictionary Use Cases
'''
Config / settings data রাখা

JSON data handle করা

Nested dictionary দিয়ে database-like structure তৈরি করা

Dictionary comprehension দিয়ে দ্রুত ডাটা process করা

Dictionary Methods:

keys(), values(), items()

update(), pop(), popitem(), clear(), copy()

fromkeys(), setdefault()

Features:

Mutable

Unordered (Python 3.7+ এ insertion order ধরে রাখে)

Key must be immutable, values যেকোনো কিছু হতে পারে

Nested dictionaries possible

Dictionary comprehension
'''

# Strings Again
# String Compare
# 1. সরাসরি == (equal operator)
s1 = "apple"
s2 = "apple"
s3 = "Apple"

print(s1 == s2)   # True (কারণ পুরোপুরি এক)
print(s1 == s3)   # False (কারণ ছোট হাতের a আর বড় হাতের A আলাদা ধরা হয়)

# 2. != (not equal operator)
s1 = "banana"
s2 = "orange"

print(s1 != s2)   # True (কারণ banana আর orange এক না)

# 3. <, > (alphabetical order / dictionary order) Python এ string গুলো alphabetical order অনুযায়ী compare হয় (ASCII value ধরে)।
print("apple" < "banana")   # True  (apple আগে আসে)
print("grape" > "banana")   # True  (grape পরে আসে)
print("Apple" < "apple")    # True  (বড় হাতের অক্ষর ছোট হাতের আগে আসে)

# 4. lower() / upper() ব্যবহার করে case-insensitive compare
s1 = "HELLO"
s2 = "hello"

print(s1.lower() == s2.lower())   # True
print(s1.upper() == s2.upper())   # True

# 5. startswith() / endswith() দিয়ে check করা
word = "Bangladesh"

print(word.startswith("Ban"))   # True
print(word.endswith("desh"))    # True


# 6. in / not in দিয়ে substring check
sentence = "I love Python"

print("Python" in sentence)     # True
print("Java" not in sentence)   # True

'''
== / != → এক বা ভিন্ন

< / > → dictionary/alphabetical order

.lower() / .upper() → case-insensitive compare

.startswith() / .endswith() → শুরু/শেষ চেক

"sub" in main → substring চেক
'''

# Escape Sequence
'''
Escape sequence হলো special characters যেগুলো string এর মধ্যে ব্যবহার করা যায়।
এগুলো \ (backslash) দিয়ে শুরু হয়। এগুলো মূলত string এর মধ্যে নতুন লাইন, tab, quote, backslash ইত্যাদি দেখানোর জন্য ব্যবহার করা হয়।
'''
# Common Escape Sequences
'''
1. \n → New Line
নতুন লাইনে চলে যাবে।
'''
text = "Hello\nWorld"
print(text)
'''
Output
------
Hello
World
'''

'''
2. \t → Tab Space
Tab space (4-8 spaces) যোগ করে।
'''
text = "Name:\tSourav"
print(text)

'''
Output
------
Name:   Sourav
'''

'''
3. \ → Backslash
একটা আসল backslash দেখাতে।
'''
text = "This is a backslash: \\"
print(text)
'''
Output
------
This is a backslash: \
'''

'''
4. ' → Single Quote
String এর মধ্যে single quote বসাতে।
'''
text = 'It\'s a book'
print(text)

'''
Output
------
It's a book
'''

# 5. " → Double Quote String এর মধ্যে double quote বসাতে।
text = "He said: \"Hello!\""
print(text)

'''
Output 
------
He said: "Hello!"
'''

# 6. \r → Carriage Return Cursor লাইন এর শুরুতে চলে যায়, পরের অংশ আগেরটা replace করে।
text = "Hello\rWorld"
print(text)
'''
Output
------
World
(কারণ "World" replace করেছে "Hello" এর উপর)
'''

# 7. \b → Backspace এক ধাপ পেছনে গিয়ে character মুছে ফেলে।
text = "Hello\bWorld"
print(text)
# HellWorld

# 8. \f → Form Feed কম ব্যবহার হয়, কিছু interpreter এ নতুন page এর মত behave করে।
text = "Hello\fWorld"
print(text)

# 9. \ooo → Octal value দিয়ে character
text = "\110\145\154\154\157"   # H e l l o
print(text)
'''
Hello
'''

# 10. \xhh → Hexadecimal value দিয়ে character
text = "\x48\x65\x6C\x6C\x6F"
print(text)
# Hello
# সবচেয়ে বেশি ব্যবহার হয় – \n, \t, \\, \', \"





