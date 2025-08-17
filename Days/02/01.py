# Program to check if a person is eligible to vote based on age
age = int(input("Enter Your Age: ")) 
nationality = int(input("Enter Your Nationality(1 for Bangladeshi, 0 for Foreigner): "))

if age >= 18 and nationality == 1:
    print("You are eligible to vote.")

else:
    print("You are not eligible to vote.")


# Program to determine the grade based on marks
marks = int(input("\nEnter Your Marks: "))

if marks >= 80 and marks <=100:
    print("You got A+")

elif marks >= 70:
    print("You got A")

elif marks >= 60:
    print("You got A-")

elif marks >= 50:
    print("You got B")

elif marks >= 40:
    print("You got C")

elif marks >= 33:
    print("You got D")

elif marks < 33:
    print("You got F")

else:
    print("Invalid Marks")


# Even or Odd Number Check
number = int(input("\nEnter a number to check if it is even or odd: "))
if number % 2 == 0:
    print("The number is even.")            
else:
    print("The number is odd.")