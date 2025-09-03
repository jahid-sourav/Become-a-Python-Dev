'''
Loop
----
Guess the Number Game (while loop): 
Consider a random number between 1 and 10. Let user guess until correct. Give hints:“Too high” or “Too low”.
'''
import random
correct_number = random.randint(1, 10)
while True:
    try:
        guess = int(input('Guess a number between 1 and 10: '))
        if guess < 1 or guess > 10:
            print('Please enter a number between 1 and 10.')
        elif guess > correct_number:
            print('Too high!')
        elif guess < correct_number:
            print('Too low!')    
        else:
            print('Congratulations! You guessed the number!')
            break       
    except ValueError:
        print('Invalid input. Please enter a number between 1 and 10.')