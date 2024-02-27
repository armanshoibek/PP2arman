import re

def match_pattern(text):
    pattern = r'ab*'  
    matches = re.findall(pattern, text)
    return matches

with open("row.txt", "r") as file:
    text = file.read()

matched_strings = match_pattern(text)

print("Strings with 'a' followed by zero or more 'b's:")
for match in matched_strings:
    print(match)
