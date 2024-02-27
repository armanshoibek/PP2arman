import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, text)
    return sequences

text = input("Enter a string: ")
sequences = find_sequences(text)
print("Sequences found:", sequences)
