import re

def camel_to_snake(camel_str):
    snake_case = re.sub('([A-Z][a-z]+)', r'_\1', camel_str).lower()
    return snake_case.lstrip('_')

camel_case_string = input("Enter camel case string: ")
snake_case_string = camel_to_snake(camel_case_string)
print("Snake case string:", snake_case_string)
