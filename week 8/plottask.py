# Write a program called plottask.py that displays: Week task 8
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.
# Some marks will be given for making the plot look nice (legend etc).

# Autor - Ianara Fernandes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution
mean = 5
std_dev = 2
sample_size = 1000
normal_values = np.random.normal(mean, std_dev, sample_size)

# Create a figure with two y-axes
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

# Plot the histogram
ax1.hist(normal_values, bins=30, density=True, alpha=0.6, color='blue', label='Normal Distribution')

# Define the function h(x) = x^3
x_values = np.linspace(0, 10, 100)
h_values = x_values**3

# Plot h(x) = x^3 on the secondary y-axis
ax2.plot(x_values, h_values, color='red', label='h(x) = x^3')

# Add labels and title
ax1.set_xlabel('x')
ax1.set_ylabel('Density (Histogram)')
ax2.set_ylabel('h(x) = x^3', color='red')
plt.title('Histogram of Normal Distribution and h(x) = x^3')

# Show the plot
plt.grid(True)
plt.show()


# Result of this task is a Histogram figure that show the distribution.