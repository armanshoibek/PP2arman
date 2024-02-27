import re

def match_pattern(text):
    pattern = r'a.*b$'
    if re.match(pattern, text):
        return True
    else:
        return False

text = input("Enter a string: ")
if match_pattern(text):
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")
