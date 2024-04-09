import numpy as np
import matplotlib.pyplot as plt

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