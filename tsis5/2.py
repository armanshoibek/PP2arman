import re

def match_pattern(text):
    pattern = r'ab{2,3}'  
    matches = re.findall(pattern, text)
    return matches

with open("row.txt", "r") as file:
    text = file.read()

matched_strings = match_pattern(text)

print("Strings with 'a' followed by two to three 'b's:")
for match in matched_strings:
    print(match)
