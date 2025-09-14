# List
numbers = [12, 13, 15, 17, 19]
# Sum
sum = 0
for num in numbers:
    sum+= num
print(sum)

# Largest
largest = numbers[0]
lowest = numbers[0]
for num in numbers:
    if(num > largest):
        largest =  num
    elif(num < lowest):
        lowest = num

    
print(f"The Largest Number is {largest} and Lowest Number is {lowest}.")

numbers_1 = [12, 13, 15, 17, 19, 19, 15, 12]
unique_list = []
for num in numbers_1:
    if num not in unique_list:
        unique_list.append(num)

for num in unique_list:
    print(num)


lists = (12, 13, 15, 17, 19, 19, 15, 12)
evenCount = 0
oddCount = 0
for num in lists:
    if num % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    
print("Total Even Numbers :", evenCount, "and Total Odd Number: ", oddCount)

try:
    userInput = int(input("Enter Your Number: "))
    countInNumber = lists.count(userInput)
    print(f"{countInNumber} times in the lists.")
except ValueError:
    print("Please valid Input Number")


numberCount = {}
for num in lists:
    if num in numberCount:
        numberCount[num] += 1
    else:
        numberCount[num] = 1
print(numberCount)

fruitsDictionary = {"mango": 2, "banana": 1, "apple": 50}
fromUserData = input("Enter The Fruit Quantity: ")  
foundKey = None

try:
    user_input = int(fromUserData)  
    for key in fruitsDictionary:
        if fruitsDictionary[key] == user_input:
            foundKey = key
            break
    if foundKey:
        print(foundKey)
    else:
        print("No fruit found with that value")
except ValueError:
    print("Please enter a valid number")

# Max Value and Key using Dictionary:
maxKey = None
maxVal = None
for key in fruitsDictionary:
    if maxVal is None or fruitsDictionary[key] > maxVal:
        maxVal = fruitsDictionary[key]
        maxKey = key

print(maxKey, maxVal)

str1 = "I Love Python"
vowels = "aeiouAEIOU"
vowel_count = 0

for character in str1:
    if character in vowels:
        vowel_count += 1
print(f"Numbers of Vowel:{vowel_count}")

# Palindrome
user_text = input("Enter your Word: ")
reversed_user_text = user_text[::-1].lower()
if user_text.lower() == reversed_user_text:
    print("This is a Palindrome Word!")
else:
    print("This is not a Palindrome Word!")

full_string = ""
for character in user_text:
    if character != " ":
        full_string += character
print(full_string)