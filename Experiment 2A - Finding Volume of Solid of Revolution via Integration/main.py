import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function definition
def f(x):
    return np.sqrt(x)

# Axis of revolution
yr = 1

# Limits of integration
a, b = 0, 4

# Calculate Volume of revolution using the disk method
def integrand(x):
    return np.pi * (f(x) - yr)**2

volume, _ = quad(integrand, a, b)

# Display the result
print(f"Volume of the solid of revolution is: {volume:.4f}")

# Discretization for visualization
x_vals = np.linspace(a, b, 101)
fx_vals = f(x_vals)

# Create 3D cylinder-like surface for visualization
theta = np.linspace(0, 2*np.pi, 50)
x_grid, theta_grid = np.meshgrid(x_vals, theta)
r_grid = f(x_grid) - yr  # Radial distance from axis of revolution

# Convert polar coordinates (r, theta) to Cartesian coordinates (Y, Z)
Y = (r_grid) * np.cos(theta_grid)
Z = (r_grid) * np.sin(theta_grid)
X = x_grid  # X corresponds to the original x-axis values

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot surface of revolution
ax.plot_surface(X, Y + yr, Z, color='b', alpha=0.6)

# Plot axis of revolution
ax.plot([a, b], [yr, yr], [0, 0], '-r', linewidth=2)

# Labels and view
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
ax.view_init(elev=22, azim=11)

plt.show()
