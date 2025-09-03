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