# Recursive Function
# Factorial = n * (n-1) 

# Factorial 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

x = int(input("Enter a number: "))
print(f"The factorial of {x} is {factorial(x)}")

# Fibonacci Sequence
# Fibonacci = F(n) = F(n-1) + F(n-2)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

y = int(input("Enter a number to find its Fibonacci: "))
print(f"The {y}th Fibonacci number is {fibonacci(y)}")

# Sum of Numbers
def sum_of_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

z = int(input("Enter a number to find the sum of numbers up to it: "))
print(f"The sum of numbers up to {z} is {sum_of_numbers(z)}")

# Power of a Number
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)  
    
a = int(input("Enter the base number: "))
b = int(input("Enter the exponent: "))
print(f"{a} raised to the power of {b} is {power(a, b)}")

# Memoization for Fibonacci
memo = {}
def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
        return memo[n]

c = int(input("Enter a number to find its Fibonacci using memoization: "))
print(f"The {c}th Fibonacci number using memoization is {fibonacci_memo(c)}")

# Variable Scope
# Local 
def greet():
    message = 'Hello'
    print('Local', message)
greet()

# Global
message = 'Hi'
def greet_global():
    print('Global', message)
greet_global()

# Nonlocal
def outer():
    message = 'Hey'
    def inner():
        nonlocal message
        message = 'Hello from inner'
        print('Inner', message)
    inner()
    print('Outer', message)
outer()