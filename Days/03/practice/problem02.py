'''
Conditional Statement
---------------------
Quadrant Identifier: 
Write a Python program that takes the coordinates (x, y) of a point as input and prints out which quadrant it belongs to (1st, 2nd, 3rd, or 4th).
'''
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("The point is in the 1st Quadrant (Q1).")
elif x < 0 and y > 0:
    print("The point is in the 2nd Quadrant (Q2).")
elif x < 0 and y < 0:
    print("The point is in the 3rd Quadrant (Q3).")
elif x > 0 and y < 0:
    print("The point is in the 4th Quadrant (Q4).")
elif x == 0 and y == 0:
    print("The point is at the Origin.")
elif x == 0:
    print("The point lies on the Y-axis.")
elif y == 0:
    print("The point lies on the X-axis.")
