# messing with files
# Author: Ianara Fernandes

import os

filename = "messingfiles"

if os.path.exists(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line, end='')

else:
    print(filename, "does not exist") 

# os.remove("data")           




filename= 'data.txt'

with open(filename, 'r') as f:
    for data in f: 
        # print(data , end="")
        print(data.strip())  
        print(data[:-1])