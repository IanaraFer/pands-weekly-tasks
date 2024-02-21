# program that reads in two numbers and
# outputs the integer answer and remainder
x = int("10")
y = int("3")
answer = int(x//y) # // gives the int division
remainder = x%y # % gives the remainder
print("{} divided by {} is {} with remainder {}".format( x, y,
answer, remainder))