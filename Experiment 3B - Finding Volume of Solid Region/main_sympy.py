import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbols
x, y = sp.symbols('x y')

# Define the function
f = sp.sin(x) * sp.cos(y)

# Perform the double integral
integral = sp.integrate(sp.integrate(f, (x, 0, sp.pi / 2)), (y, 0, sp.pi / 2))
print(f"Double integral result: {integral}")

# Visualization (3D plot)
x_vals = np.linspace(0, np.pi / 2, 100)
y_vals = np.linspace(0, np.pi / 2, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.sin(X) * np.cos(Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Labeling
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z = sin(x)*cos(y)')
plt.title('Surface plot of sin(x)*cos(y)')

plt.show()
