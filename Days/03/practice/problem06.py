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
    