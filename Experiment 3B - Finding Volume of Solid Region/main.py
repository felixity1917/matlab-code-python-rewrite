import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Define the function to be integrated
def f(x, y):
    return np.sin(x) * np.cos(y)

# Compute the double integral using scipy.integrate.dblquad
result, error = integrate.dblquad(f, 0, np.pi/2, lambda x: 0, lambda x: np.pi/2)
print(f"Double integral result: {result}")

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
