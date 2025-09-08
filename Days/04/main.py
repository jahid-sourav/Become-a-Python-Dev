# List, Tuple, Dictionary and Strings

# List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
print(my_list[0])
print(my_list[-1])

# Slicing
print(my_list[1:4])
print(my_list[:3])
print(my_list[2:])
print(my_list[:])

# Length
print("Length of list:", len(my_list))

# Membership
print(3 in my_list)
print(30 in my_list)

# Append
my_list.append(6)   
print("After append:", my_list)

# Insert
my_list.insert(0, 0)
print("After insert:", my_list)

# Extend
my_list.extend([7, 8, 9, 10, 11])   
print("After extend:", my_list)

# Delete
del my_list[11]
print("After delete:", my_list)

del my_list[5:6]
print("After delete slice:", my_list)

del my_list[-1] 
print("After delete last element:", my_list)

# Remove
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
languages.remove('R')
print("After remove:", languages)

# List Comprehension
squared = [x**2 for x in range(10)] 
print("List comprehension (squared):", squared)

# Tuple
my_tuple = (1, 2, 3, 4, 5)  
print("Tuple:", my_tuple)
print(my_tuple[0])

# Dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Dictionary:", my_dict)

# Strings
my_string = "Hello, World!"
print("String:", my_string) 
print(my_string[0])
print(my_string[-1])
print(my_string[7:12])
print("Length of string:", len(my_string))

# Compare Strings
print("apple" < "banana")   
print("grape" > "banana")
print("apple" == "apple")
print("apple" != "banana")
print("apple" <= "Apple")
print("apple" >= "Apple")
print("apple" <= "banana")
print("apple" >= "banana")

# String Methods
print(my_string.lower())    
print(my_string.upper())
print(my_string.replace("World", "Python"))
print(my_string.split(", "))
print(my_string.find("World"))
print(my_string.count("o"))
print(my_string.startswith("Hello"))    
print(my_string.endswith("!"))
print(my_string.strip("!"))
print(" ".join(["Hello", "from", "Python"]))
print(my_string.isalpha())
print("12345".isdigit())
print("Hello123".isalnum())
print(my_string.capitalize())
print(my_string.title())
print(my_string.center(30, '-'))
print(my_string.ljust(30, '-'))
print(my_string.rjust(30, '-'))
print(my_string.zfill(20))
print(my_string.encode())
print(my_string.format(name="Alice"))
print(my_string.partition(", "))
print(my_string.rpartition(", "))
print(my_string.swapcase())
print(my_string.translate(str.maketrans("Helo", "Jxyz")))
print(my_string.removeprefix("Hello"))
print(my_string.removesuffix("!"))
print(my_string.islower())
print(my_string.isupper())
print(my_string.isspace())
print(my_string.expandtabs(tabsize=4))
print(my_string.casefold())
print(my_string.isprintable())
print(my_string.splitlines())
print(my_string.rsplit(", "))
print(my_string.lstrip("H"))
print(my_string.rstrip("!"))
print(my_string.encode('utf-8'))
print(my_string.decode('utf-8', 'ignore'))
print(my_string.__add__(" How are you?"))
print(my_string.__contains__("World"))
print(my_string.__len__())
print(my_string.__getitem__(7))
print(my_string.__setitem__(7, 'w'))  # Note: Strings are immutable
print(my_string.__delitem__(7))       # Note: Strings are immutable
print(my_string.__iter__())
print(my_string.__reversed__())
print(my_string.__str__())
print(my_string.__repr__())
print(my_string.__format__("")) 
print(my_string.__hash__())
print(my_string.__sizeof__())
print(my_string.__dir__())
print(my_string.__doc__)        
print(my_string.__class__)
print(my_string.__module__)

# Escape Sequences
print("Newline:\nHello")        
print("Tab:\tHello")
print("Backslash:\\Hello")
print("Single Quote:\'Hello\'")
print("Double Quote:\"Hello\"")
print("Carriage Return:\rHello")
print("Backspace:Hello\bWorld")
print("Form Feed:\fHello")
print("Unicode Character:\u03A9")
print("Raw String: r\"Hello\nWorld\"")
print(r"Raw String: Hello\nWorld")
print("Octal Character:\101")
print("Hexadecimal Character:\x41") 
print("Bell Character:\aHello")
print("Vertical Tab:\vHello")   
print("Null Character:\0Hello")
print("String with multiple escape sequences:\n\tHello, \"World\"!\n")      
print("String with raw and escape sequences: r\"Hello\\nWorld\"\n")
print(r"String with raw and escape sequences: Hello\nWorld\n")
print("String with Unicode and escape sequences: \u03A9 is Omega\n")
print("String with octal and hexadecimal characters: \101 and \x41\n")
print("String with bell and vertical tab characters: \aHello\vWorld\n")

# Multi-line Strings
multi_line_string = """This is a
multi-line string."""
print("Multi-line String:", multi_line_string)              
raw_multi_line_string = r"""This is a
raw multi-line string."""   
print("Raw Multi-line String:", raw_multi_line_string)
escaped_multi_line_string = """This is a multi-line string with escape sequences:\n\tHello, "World"!\n"""
print("Escaped Multi-line String:", escaped_multi_line_string)
raw_escaped_multi_line_string = r"""This is a raw multi-line string with escape sequences
:\n\tHello, "World"!\n"""
print("Raw Escaped Multi-line String:", raw_escaped_multi_line_string)    

# String Formatting
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print("Formatted String:", formatted_string)
f_string = f"My name is {name} and I am {age} years old."
print("F-String:", f_string)

# Old Style Formatting
old_style_string = "My name is %s and I am %d years old." % (name, age)
print("Old Style Formatted String:", old_style_string)  
percent_string = "I have 100%% confidence in my skills."
print("Percent String:", percent_string)    
number_string = "The number is %f." % 3.14159
print("Number String:", number_string)
precision_string = "The number with 2 decimal places is %.2f." % 3.14159
print("Precision String:", precision_string)
width_string = "The number with width 10 is %10.2f." % 3.14159
print("Width String:", width_string)
left_justified_string = "The number left justified with width 10 is %-10.2f." % 3.14159
print("Left Justified String:", left_justified_string)
zero_filled_string = "The number zero filled with width 10 is %010.2f." % 3.14159
print("Zero Filled String:", zero_filled_string)
scientific_string = "The number in scientific notation is %e." % 3.14159
print("Scientific String:", scientific_string)
hex_string = "The number in hexadecimal is %x." % 255
print("Hexadecimal String:", hex_string)
octal_string = "The number in octal is %o." % 255   
print("Octal String:", octal_string)
character_string = "The character for ASCII 65 is %c." % 65             
print("Character String:", character_string)

