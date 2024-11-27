import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Function definitions
def f(x):
    return 2 - x**2  # Upper curve

def g(x):
    return -x  # Lower curve

# Limits of integration
a, b = -1, 2

# Calculate Area
Area, _ = quad(lambda x: f(x) - g(x), a, b)

# Display the result
print(f'Area bounded by the curves f(x) and g(x) is: {Area:.4f}')

# Discretization for plotting
x_vals = np.linspace(a, b, 20)
y1_vals = f(x_vals)
y2_vals = g(x_vals)

# Plot the graphs
plt.plot(x_vals, y1_vals, label='f(x)')
plt.plot(x_vals, y2_vals, label='g(x)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()
