# Program to subtract on number from another.
# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations
from multiprocessing import Value


x = int("10")
y = int("4")
answer= x-y
print ("{} minus {} is {}".format(x, y, answer))