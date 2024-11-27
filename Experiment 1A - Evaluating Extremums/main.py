import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return np.sin(np.abs(x))

# Discretization
a, b = -2 * np.pi, 2 * np.pi
t = np.linspace(a, b, 10000)

# Finding the points
g = f(t)  # Finding the values of f(x) at t values
loc_max, _ = find_peaks(g)  # Just get the indices of the local maxima
lmax_x = np.round(t[loc_max], 4)

h = -g  # For local minima, use the negative of the function
loc_min, _ = find_peaks(h)  # Just get the indices of the local minima
lmin_x = np.round(t[loc_min], 4)

# Display the values
print('Local maximum occurs at x=')
print(lmax_x)
print('The Local Maximum value(s) of the function are ')
print(np.round(f(lmax_x), 4))

print('Local minimum occur at x=')
print(lmin_x)
print('The local Minimum Value(s) of the function are ')
print(np.round(f(lmin_x), 4))

# Plot the graphs
plt.plot(t, g, label='f(x)')  # Plotting the function
plt.plot(lmax_x, f(lmax_x), 'or', label='Local Maxima')  # Pointing the local maxima
plt.plot(lmin_x, f(lmin_x), '*g', label='Local Minima')  # Pointing the local minima
plt.legend()
plt.show()
