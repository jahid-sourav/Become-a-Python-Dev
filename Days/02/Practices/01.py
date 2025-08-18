# Leap Year
user_input = int(input("Enter a year: "))
if((user_input % 4 == 0 and user_input % 100 != 0) or (user_input % 400 == 0)):
    print(f"{user_input} is a leap year.")
else:
    print(f"{user_input} is not a leap year.")

# Vowel or Consonant
given_char = input("Enter a character: ").lower()
if(given_char > "a" and given_char < "z"):
    if(given_char in 'aeiou'):
        print(f"{given_char} is a vowel.")
    else:
        print(f"{given_char} is a consonant.")  
else:
    print("Invalid input. Please enter a single alphabet character.")

