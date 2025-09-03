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