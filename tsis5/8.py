import re

def split_at_uppercase(string):
    words = re.findall('[A-Z][a-z]*', string)
    return words

input_string = input("Enter a string: ")
result = split_at_uppercase(input_string)
print("Result:", result)
