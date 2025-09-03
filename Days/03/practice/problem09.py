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


