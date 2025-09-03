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