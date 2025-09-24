# List Problems
#1
def split_positive_negative(nums):
    positive = []
    negative = []
    for num in nums:
        if num > 0:
            positive.append(num)
        elif num < 0:
            negative.append(num)
    return positive, negative

numbers = [-2, 5, 0, -8, 3, -1, 7]
pos, neg = split_positive_negative(numbers)
print("Positive:", pos)  
print("Negative:", neg)  

# 2
def second_largest(nums):
    if len(nums) < 2:
        return None
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second


nums = [1, 3, 5, 4, 2]
print(f"Second largest Number is {second_largest(nums)}")  

# 3
def rotate_list(nums, k):
    k = k % len(nums)  
    return nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5]
print(f"Rotated List: {rotate_list(nums, 2)}") 

# Dictionaries
# 1
def frequency_counter(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

nums = [1, 2, 2, 3, 1]
print(f"Frequency Count: {frequency_counter(nums)}")  

# 2
def high_scorers(grades):
    for name, mark in grades.items():
        if mark > 80:
            print(name)

grades = {"Jahid": 85, "Sourav": 70, "Israt": 90}
high_scorers(grades) 

# 3
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted

d = {"a": 1, "b": 2}
print(f"Inverted Dictionary: {invert_dict(d)}") 

# 4
def word_lengths(words):
    length_dict = {}
    for word in words:
        length_dict[word] = len(word)
    return length_dict

words = ["apple", "banana", "cat"]
print(f"Word Lengths: {word_lengths(words)}")  

# Tuples
# 1
def tuple_max_min(tup):
    if not tup:
        return None, None
    max_val = min_val = tup[0]
    for num in tup:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

tup = (1, 3, 5, 2)
print(f"Max: {tuple_max_min(tup)[0]}, Min: {tuple_max_min(tup)[1]}")

# 2
def find_index(tup, elem):
    for i in range(len(tup)):
        if tup[i] == elem:
            return i
    return -1  

tup = (1, 2, 3, 2)
print(f"Index of 2: {find_index(tup, 2)}") 

# 3
def swap_tuple_elements(tuple_list):
    result = []
    for tup in tuple_list:
        if len(tup) >= 2:
            swapped = (tup[-1],) + tup[1:-1] + (tup[0],)
            result.append(swapped)
        else:
            result.append(tup)
    return result

tuple_list = [(1, 2, 3), (4, 5)]
print(f"Swapped Tuples: {swap_tuple_elements(tuple_list)}") 

# 4
def even_sum_pairs(tup):
    for i in range(len(tup)):
        for j in range(i+1, len(tup)):
            if (tup[i] + tup[j]) % 2 == 0:
                print((tup[i], tup[j]))

tup = (1, 2, 3, 4, 5)
even_sum_pairs(tup) 

# 5
def concat_tuples(tup1, tup2):
    result = []
    for elem in tup1:
        result.append(elem)
    for elem in tup2:
        result.append(elem)
    return tuple(result)

tup1 = (1, 2)
tup2 = (3, 4)
print(f"Concatenated Tuple: {concat_tuples(tup1, tup2)}") 

# Strings
# 1
def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

print(is_palindrome("radar"))  
print(is_palindrome("hello")) 

# 2
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_word = ''
        for char in word:
            reversed_word = char + reversed_word
        reversed_words.append(reversed_word)
    return ' '.join(reversed_words)

sentence = "hello world"
print(f"Reversed Words: {reverse_words(sentence)}") 

# 3
def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

s = "hello"
print(f"Character Frequency: {char_frequency(s)}")  

# 4
def remove_duplicates(s):
    seen = {}
    result = ''
    for char in s:
        if char not in seen:
            seen[char] = True
            result += char
    return result

s = "hello"
print(f"String without duplicates: {remove_duplicates(s)}")  

# 5
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1
    return freq1 == freq2


print(f"Are 'listen' and 'silent' anagrams? {is_anagram('listen', 'silent')}")  
print(f"Are 'hello' and 'world' anagrams? {is_anagram('hello', 'world')}") 

# Sets
# 1
def unique_words(sentence):
    words = sentence.split()
    return set(words)

sentence = "hello world hello"
print(f"Unique Words: {unique_words(sentence)}") 

# 2
def common_elements(list1, list2):
    set1 = set(list1)
    common = []
    for elem in list2:
        if elem in set1:
            common.append(elem)
    return common

list1 = [1, 2, 3]
list2 = [2, 3, 4]
print(f"Common Elements: {common_elements(list1, list2)}")  

# 3
def manual_union(set1, set2):
    result = set()
    for elem in set1:
        result.add(elem)
    for elem in set2:
        result.add(elem)
    return result

set1 = {1, 2}
set2 = {2, 3}
print(f"Union: {manual_union(set1, set2)}") 

# 4
def missing_number(num_set, n):
    full_sum = n * (n + 1) // 2
    actual_sum = 0
    for num in num_set:
        actual_sum += num
    return full_sum - actual_sum

num_set = {1, 2, 4, 5} 
print(f"Missing Number: {missing_number(num_set, 5)}") 