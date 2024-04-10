# Task week 7. Count the letter 'e' in the first capitel of the book moby dick.
# author - Ianara Fernandes
# Read the text from the file (assuming 'moby-dick.txt' is in the same directory)

FILENAME: 'moby'
def new_func():
    with open('mobidick', 'r') as f:
        text = f.read()

# Count the occurrences of the letter 'e'
    e_count = text.lower().count('e')

    print(f"The letter 'e' appears {e_count} times in the text.")

new_func()