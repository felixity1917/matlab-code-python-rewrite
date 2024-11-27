import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the function and constraint
def f(x, y):
    return x**2 + y**2

def g(x, y):
    return x + y - 10  # g(x) = 0

# Define the Lagrangian with lambda (L) as the multiplier
def lagrangian(vars):
    x, y, L = vars
    return [
        2 * x + L,  # Partial derivative with respect to x
        2 * y + L,  # Partial derivative with respect to y
        x + y - 10  # The constraint equation
    ]

# Solve the system of equations
initial_guess = [1, 1, 1]
solution = fsolve(lagrangian, initial_guess)

x_sol, y_sol, L_sol = solution
print(f"Stationary point: x = {x_sol}, y = {y_sol}")
print(f"Function value at stationary point: f(x, y) = {f(x_sol, y_sol)}")

# Visualization
X = np.linspace(x_sol - 3, x_sol + 3, 20)
Y = np.linspace(y_sol - 3, y_sol + 3, 20)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

# Surface plot of f(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)

# Plot the constraint g(x, y) = 0 (as a line)
gv_x = np.linspace(x_sol - 3, x_sol + 3, 100)
gv_y = 10 - gv_x  # From the equation x + y = 10
gv_y[np.isnan(gv_y)] = 0  # Avoid division by zero (when x=0)
fv_z = f(gv_x, gv_y)

# Plot the constraint in red
ax.plot(gv_x, gv_y, fv_z, 'r-', label='g(x, y) = 10')
ax.scatter(x_sol, y_sol, f(x_sol, y_sol), color='black', s=100, label='Stationary Point')

# Labels and legend
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.legend()
plt.show()
