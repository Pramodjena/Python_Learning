# Strings:

single_quoted_string = "Hey, I am Pramod"

double_quoted_string = "Hey, I am Pramod"

multiline_single_quoted_string = """ Hey, I am Pramod
and 
I am a developer"""

multiline_double_quoted_string = """Hey, 
I 
am
Pramod
"""


# print(single_quoted_string)
# print(double_quoted_string)
# print(multiline_single_quoted_string)
# print(multiline_single_quoted_string)


""" 
This is multi-line comment

"""


# Concatenation:

str1 = "Hello"
str2 = "world"
concatenate_string = str1 + " " + str2
# print(concatenate_string)


# String length:

myName = "Pramod Kumar Jena"

# print(len(myName))

# Indexing and slicing:

"""
Index:  | 0  |  1 |  2 |  3 |  4 | 5  |
        _______________________________
Char:   | P  |  y |  t |  h |  o |  n | 
        _______________________________
Neg-Idx:| -6 | -5 | -4 | -3 |  -2| -1 |  

"""

language = "Python"
# print(language[0])  # prints 'P'
# print(language[-0])  # prints 'P'
# why is it -0? coz in mathematically 0 and -0 has same value so it here it treats as 0 === -0
# print(language[-6])  # prints 'P'


myName = "Pramod Kumar Jena"
# print(myName[0])  # prints 'P'
# print(myName[18])  # prints 'P' IndexError: string index out of range
# print(myName[-1])  # prints 'a' from last index

# Substring:

# print(myName[0:6])  # prints 'Pramod'


filename = "image.jpg"
extension = filename[-3:]
# print(extension)  # "jpg"

# palindrome
palindrome = "madam"
# print(palindrome == palindrome[::-1])  # prints True


# String formatting:

name = "Pramod"
age = 26
year = 2025

print(f"My name is {name} and I am {age} years old.")
print(f"My name is {name} and I am {age} in {year}")
print("My name is {0} and I am {1} years old.".format("Pramod", 26))
print("Hello %s!! you have %d messages and your energy is %f." % ("Pramod", 10, 92.56))


# Escape chars

print("\nHey\n I am Pramod\n I am coding.\t ...")
