import math

# Set
a = {1, 2, 3, 4, 5, 6, 1, 2, 3}
b = {3, 5, 7, 11, 9}

# Add
a.add(0)
print(a)

# Remove
a.remove(6)
a.discard(5)
print(a)

# Membership
if 1 in a:
    print("1 in A")
else:
    print("No")

c = {1, 2, 3, 4, 5, 6}
d = {3, 5, 7, 11, 9}

# Union Set
print(c | d)
print(c.union(d))

# Intersection Set
print(c & d)
print(c.intersection(d))

# Difference Set
print(c - d)
print(c.difference(d))

# Symmetric Difference
print(c ^ d)
print(c.symmetric_difference(d))

# List to Set
numbers = [1,2,3,4,5,6,6,7,8,54,2,1,3,4,5,671,2345,2,1,34,5,6]
unique_numbers = set(numbers)
print(unique_numbers)

# Find Duplicates
duplicates = (c.intersection(d))
print(duplicates)

# Functions
def sum (a, b):
    return a + b

first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))

print(f"The Sum is {sum(first_number, second_number)}")

print(f"{int(math.sqrt(first_number))}")

# Lambda (Anonymous Function)
print_sum = lambda a, b, c: a + b + c
print(print_sum(1, 2, 3))

# Unique Elements List using Function
def unique_elements(given_list):
    unique_lists = []
    
    for i in given_list:
        if i not in unique_lists:
            unique_lists.append(i)
    return unique_lists

print(f"The Unique Elements List is: {unique_elements(numbers)}")