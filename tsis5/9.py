import re

def insert_spaces(string):
    modified_string = re.sub(r"(\w)([A-Z])", r"\1 \2", string)
    return modified_string

input_string = input("Enter a string: ")
result = insert_spaces(input_string)
print("Modified string:", result)
