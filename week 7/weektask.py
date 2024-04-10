import sys
import os

def count_words(filename):
    try:
        # Check if the file exists
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist.")
            return

        # Check if the file is a text file
        if not filename.lower().endswith(".txt"):
            print(f"Error: '{filename}' is not a text file.")
            return

        # Read the file and count the words
        with open(filename, "r") as file:
            content = file.read()
            word_count = len(content.split())
            print(f"Word count in '{filename}': {word_count}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python es.py <filename>")
    else:
        filename_arg = sys.argv[1]
        count_words(filename_arg)
