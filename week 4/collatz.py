# collatz.py

number = 10
x = int(10 / 2)
y = int(x * 3 + 1) 
z = int(y / 2)
h = int(z / 2)
g = int(h / 2)
i = int(g /2)
results = number,x,y,z,h,g,i
print(results, end=" ")
