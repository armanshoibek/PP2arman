[1]
import os

def display_directories_and_files(path):
    print("List of directories and files:")
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
        for directory in dirs:
            print(f"    {directory}/")
        for file in files:
            print(f"    {file}")

specified_path = input("Enter the path: ")

display_directories_and_files(specified_path)


[2]
import os

def check_path_access(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists.")
        
        if os.access(path, os.R_OK):
            print(f"Path '{path}' is readable.")
        else:
            print(f"Path '{path}' is not readable.")
        
        if os.access(path, os.W_OK):
            print(f"Path '{path}' is writable.")
        else:
            print(f"Path '{path}' is not writable.")
        
        if os.access(path, os.X_OK):
            print(f"Path '{path}' is executable.")
        else:
            print(f"Path '{path}' is not executable.")
    else:
        print(f"Path '{path}' does not exist.")

specified_path = input("Enter the path: ")

check_path_access(specified_path)



[3]
import os

def test_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

specified_path = input("Enter the path: ")

test_path(specified_path)



[4]
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"Number of lines in '{file_path}': {line_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

file_path = input("Enter the file path: ")

count_lines(file_path)


[5]
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

file_path = input("Enter the file path: ")
data = input("Enter the list (comma-separated): ").split(',')

write_list_to_file(file_path, data)
print(f"The list has been written to the file '{file_path}'.")


[6]
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("One or both files not found.")

source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

copy_file(source_file, destination_file)




[7]

import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            except OSError as e:
                print(f"Error: {e}")
        else:
            print(f"No write access to '{file_path}'. Cannot delete the file.")
    else:
        print(f"File '{file_path}' does not exist.")

file_path = input("Enter the file path: ")

delete_file(file_path)