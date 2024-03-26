# w is for open and writing
# follow code

with open('readme.txt', 'w') as f:
    f.write('Create a new text file!')


# x is for open a file for exclusive creation

with open('readme.txt', 'x') as f:
    f.write('Create a new text file!')        


# To create a file in a specific directory (e.g., docs/readme.txt), ensure that the directory exists before creating the file.
# Handle exceptions if the directory doesn’t exist.
# Example
    
try:
    with open('docs/readme.txt', 'w') as f:
        f.write('Create a new text file!')
except FileNotFoundError:
    print("The 'docs' directory does not exist")   


# The 'r' mode opens the file for reading. Example:

with open('readme.txt') as f:
    lines = f.readlines()

with open('readme.txt') as f:
    content = f.read()  # Read the entire content
    line = f.readline()  # Read a single line
    lines = f.readlines()  # Read all lines into a list


# Close the File:
# Always close the file using f.close() when you’re done reading.
# Alternatively, use the with statement to automatically close the file.