'''
Loop
----
Fibonacci Sequence (for loop): 
Input N. Print the first N terms of the Fibonacci sequence.
'''
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer")
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ') 

        temp = a + b  
        a = b         
        b = temp  