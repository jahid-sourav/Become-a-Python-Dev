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