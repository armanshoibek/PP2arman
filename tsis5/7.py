def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_case = components[0] + ''.join(x.title() for x in components[1:])
    return camel_case

snake_case_string = input("Enter snake case string: ")
camel_case_string = snake_to_camel(snake_case_string)
print("Camel case string:", camel_case_string)
