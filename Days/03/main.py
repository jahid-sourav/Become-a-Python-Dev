# Sum
give_number = int(input("Enter a number: "))
total = 0
for i in range(1, give_number + 1):
    total += i
print(f"The sum of all numbers from 1 to {give_number} is: {total}")

# Multiplication Table
user_input = int(input("Enter A Number: "))
for i in range(1, 11):
    print(f"{user_input} x {i} = {user_input * i}")

# Factorial
factorial_number = int(input("Enter a number to calculate its factorial: "))
factorial_result = 1
while factorial_number > 1:
    factorial_result *= factorial_number
    factorial_number -= 1
print(f"The factorial is: {factorial_result}")
