from itertools import permutations

def print_permutations():
    user_input = input("Enter a string: ")
    perms = permutations(user_input)
    print("All permutations of the string:")
    for perm in perms:
        print(''.join(perm))

print_permutations()
