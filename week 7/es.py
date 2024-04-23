# Task week 7. Count the letter 'e' in the first chapter of the book moby dick. I got the first book chapter for do this task. 
# But there are 2 way to do it. One is if you have the file like I did you will have the number of 'e' in the first chapter of the book. But if you don't have the file book the program will tell you that the file was not fould.
# Author - Ianara Fernandes

from collections import Counter

FILENAME = 'moby-dick.txt'

# Read the file content
with open(FILENAME, 'r') as file:
     content = file.read()
     print(content)
# Example usage:
e_count = (FILENAME, 'e')
e_count = FILENAME.lower().count("e")
print(f"The letter 'e' appears {e_count} times in the 'moby-dick.txt' file.")

# Create a counter for all letters
letter_counts = Counter(content)

# Get the count for 'e'
e_count = letter_counts['e']

print(f"The letter 'e' appears {e_count} times in the file.")

# If the File not found
except FileNotFoundError:
    print(f"The file '{FILENAME}' is not found.")

