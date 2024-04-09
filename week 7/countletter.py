# Open the text file
with open('mobi-dick.txt') as file:
    # Read each line
    lines = file.readlines()

    # Initialize a dictionary to store letter frequencies
    freqs = {}

    # Iterate through each line
    for line in lines:
        # Filter out non-letter characters and convert to lowercase
        line = filter(lambda x: x.isalpha(), line.lower())

        # Count the occurrences of each letter
        for char in line:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1

    # Print the result
    for letter, count in freqs.items():
        if letter == 'e':
            print(f"{letter} {count}")