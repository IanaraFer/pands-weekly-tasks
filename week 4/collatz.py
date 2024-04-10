# Week task 4. asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Autor - Ianara Fernandes

number = 10
x = int(10 / 2)
y = int(x * 3 + 1) 
z = int(y / 2)
h = int(z / 2)
g = int(h / 2)
i = int(g /2)
results = number,x,y,z,h,g,i
print(results, end=" ")


# I got the result of 10, 5, 16, 8, 4, 2, 1 but they are betwen () and I could not find the way to have just numers without ()
