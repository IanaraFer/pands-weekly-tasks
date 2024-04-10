# Task week 7. Count the letter 'e' in the first capitel of the book moby dick.
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