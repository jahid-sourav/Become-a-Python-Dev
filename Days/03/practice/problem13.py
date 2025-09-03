'''
Loop
----
Password Retry System (while loop) : 
Predefined password. Let user try until correct or after 3 failed attempts show "Account locked"
'''

password = "abcd1234"
attempts = 0  

while attempts < 3:   
    user_input = input("Enter your password: ")

    if user_input == password:
        print("Access granted")
        break   
    else:
        print("Incorrect password")
        attempts += 1   

if attempts == 3:
    print("Account locked")
