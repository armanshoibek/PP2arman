import re

def find_sequences(text):
    pattern=r'b[a-z]+_[a-z]+\b'
    sequences=re.findall(pattern,text)
    return sequences

with open("row.txt", "r") as file:
    text=file.read()

found_sequences=find_sequences(text)

print("Sequences of lowercase letters joined with an underscore:")
for sequence in found_sequences:
    print(sequence)