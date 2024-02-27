def replace_with_colon(text):
    replacements = {' ': ':', ',': ':', '.': ':'}
    for old_char, new_char in replacements.items():
        text = text.replace(old_char, new_char)
    return text

input_text = input("Enter a string: ")
output_text = replace_with_colon(input_text)
print("Modified string:", output_text)
