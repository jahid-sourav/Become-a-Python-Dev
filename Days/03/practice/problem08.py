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