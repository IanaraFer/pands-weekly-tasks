# Write a program called plottask.py that displays: Week task 8
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.
# Some marks will be given for making the plot look nice (legend etc).

# Autor - Ianara Fernandes
# Plotting
import matplotlib.pyplot as plt
# Numerical arrays.
import numpy as np

# Generate 1000 random values from a normal distribution
mean = 5
std_dev = 2
sample_size = 1000
random_values = np.random.normal(mean, std_dev, sample_size)

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(random_values, bins=30, density=True, alpha=0.6, color='blue', label='Normal Distribution')

# Plot the function h(x) = x^3
x_values = np.linspace(0, 10, 100)
h_x = x_values**3
plt.plot(x_values, h_x, color='red', label='$h(x) = x^3$')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram of Normal Distribution and $h(x) = x^3$')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()