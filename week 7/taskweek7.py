# Task week 7. Count the letter 'e' in the first capitel of the book moby dick.
# author - Ianara Fernandes


# Open the text file

filename = 'mobidick.txt'

with open(filename,'r') as f:
   mobidick = f.read()
    # Read the entire content
   lines = f.readlines()

    # Count the occurrences of each letter
letter_counts = Counter(text)

    # Print the result
for letter, count in letter_counts.items():
        if letter == 'e':
            print(f"{letter} {count}")