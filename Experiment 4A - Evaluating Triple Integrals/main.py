import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate

# Define the limits
xa, xb = -2, 2

# Define ya(x) and yb(x) as functions of x
def ya(x):
    return -np.sqrt(2 - x**2 / 2)

def yb(x):
    return np.sqrt(2 - x**2 / 2)

# Define za(x, y) and zb(x, y)
def za(x, y):
    return x**2 + 3*y**2

def zb(x, y):
    return 8 - x**2 - y**2

# Define the integrand function for volume calculation
def integrand(x, y):
    z_lower = za(x, y)
    z_upper = zb(x, y)
    # Return the integral over z
    return integrate.quad(lambda z: 1, z_lower, z_upper)[0]

# Perform the double integration with x bounds and then y bounds
def volume_func(x):
    return integrate.quad(lambda y: integrand(x, y), ya(x), yb(x))[0]

volume, error = integrate.quad(volume_func, xa, xb)

print(f"Volume: {volume}")

# Visualization (3D plot)
x_vals = np.linspace(xa, xb, 100)
y_vals = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z1 = X**2 + 3*Y**2  # Lower surface
Z2 = 8 - X**2 - Y**2  # Upper surface

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surfaces
ax.plot_surface(X, Y, Z1, alpha=0.5, cmap='viridis')
ax.plot_surface(X, Y, Z2, alpha=0.5, cmap='plasma')

# Labeling
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Solid Visualization')

plt.show()
