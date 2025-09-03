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