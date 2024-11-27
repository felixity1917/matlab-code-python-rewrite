import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the function and constraint
def f(x, y):
    return x**2 + y**2

def g(x, y):
    return x * y - 5  # g(x, y) = 0, i.e., x * y = 5

# Define the Lagrangian with L (lambda) as the multiplier
def lagrangian(vars):
    x, y, L = vars
    return [
        2 * x + L * y,  # Partial derivative with respect to x
        2 * y + L * x,  # Partial derivative with respect to y
        x * y - 5  # The constraint equation
    ]

# Solve the system of equations using fsolve
initial_guesses = [[1, 1, 1], [2, 2, 1], [3, 3, 1], [-1, -1, 1], [0.1, 50, 1]]  # Multiple initial guesses
solutions = [fsolve(lagrangian, guess) for guess in initial_guesses]

# Extract and print stationary points, avoiding duplicates
stationary_points = []
for sol in solutions:
    x, y, L = sol
    f_val = f(x, y)
    # Round to a tolerance to avoid duplicates
    is_duplicate = False
    for point in stationary_points:
        if np.isclose(x, point[0], atol=1e-4) and np.isclose(y, point[1], atol=1e-4):
            is_duplicate = True
            break
    if not is_duplicate:
        stationary_points.append((x, y, f_val))

print("All stationary points:")
for x, y, f_val in stationary_points:
    print(f"Stationary point: x = {x:.4f}, y = {y:.4f}, f(x, y) = {f_val:.4f}")

# Visualization
X = np.linspace(-3, 3, 50)
Y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

# Surface plot of f(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)

# Plot the constraint g(x, y) = 0 (as a curve)
gv_x = np.linspace(-3, 3, 100)

# Avoid division by zero and calculate only for x != 0
gv_y = np.where(gv_x != 0, 5 / gv_x, np.nan)  # Set y to NaN where x = 0 to avoid division by zero

# Only plot valid points (i.e., where y is not NaN)
valid_x = gv_x[~np.isnan(gv_y)]
valid_y = gv_y[~np.isnan(gv_y)]

# Plot the constraint curve (g(x, y) = 5) in red
fv_z = f(valid_x, valid_y)

# Plot the constraint in red, ignoring NaN values
ax.plot(valid_x, valid_y, fv_z, 'r-', label='g(x, y) = x * y = 5')

# Plot stationary points
for x, y, f_val in stationary_points:
    ax.scatter(x, y, f_val, color='black', s=100)

# Labels and legend
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.legend()
plt.show()
