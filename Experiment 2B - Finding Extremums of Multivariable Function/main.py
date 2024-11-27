import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function definition
def f(x, y):
    return x**4 + y**4 - x**2 - y**2 + 1

# Partial derivatives
def fx(x, y):
    return 4 * x**3 - 2 * x

def fy(x, y):
    return 4 * y**3 - 2 * y

# Second partial derivatives (for Hessian matrix)
def fxx(x, y):
    return 12 * x**2 - 2

def fxy(x, y):
    return 0  # Mixed derivative is zero in this case

def fyy(x, y):
    return 12 * y**2 - 2

# Search for critical points using grid search
x_vals = np.linspace(-2, 2, 1000)  # Increased grid resolution
y_vals = np.linspace(-2, 2, 1000)
X, Y = np.meshgrid(x_vals, y_vals)

# Evaluate partial derivatives across the grid
FX = fx(X, Y)
FY = fy(X, Y)

# Find points where both partial derivatives are near zero (critical points)
tolerance = 1e-2  # Relaxed tolerance
critical_points = np.where((np.abs(FX) < tolerance) & (np.abs(FY) < tolerance))

ax_vals = X[critical_points]
ay_vals = Y[critical_points]

if len(ax_vals) == 0:
    print("No critical points found. Consider adjusting the tolerance or grid resolution.")
else:
    print("Critical Points (from grid search):")
    # Calculate the Hessian determinant (D = fxx * fyy - (fxy)^2) for each critical point
    for i in range(len(ax_vals)):
        ax_val = ax_vals[i]
        ay_val = ay_vals[i]
        D = fxx(ax_val, ay_val) * fyy(ax_val, ay_val) - fxy(ax_val, ay_val)**2
        T2 = fxx(ax_val, ay_val)
        T3 = f(ax_val, ay_val)

        if D < 0:
            print(f"Saddle Point at ({ax_val:.4f}, {ay_val:.4f}) with value f({ax_val:.4f}, {ay_val:.4f}) = {T3:.4f}")
        elif T2 < 0:
            print(f"Maximum at ({ax_val:.4f}, {ay_val:.4f}) with value f({ax_val:.4f}, {ay_val:.4f}) = {T3:.4f}")
        else:
            print(f"Minimum at ({ax_val:.4f}, {ay_val:.4f}) with value f({ax_val:.4f}, {ay_val:.4f}) = {T3:.4f}")

    # Visualization
    legend_labels = []  # To track which labels are already added
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    Z = f(X, Y)
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

    for i in range(len(ax_vals)):
        ax_val = ax_vals[i]
        ay_val = ay_vals[i]
        D = fxx(ax_val, ay_val) * fyy(ax_val, ay_val) - fxy(ax_val, ay_val)**2
        T2 = fxx(ax_val, ay_val)
        T3 = f(ax_val, ay_val)

        if D < 0:
            label = 'Saddle Point'
            if label not in legend_labels:
                ax.plot([ax_val], [ay_val], [T3], 'bv', markersize=10, label=label)
                legend_labels.append(label)
            else:
                ax.plot([ax_val], [ay_val], [T3], 'bv', markersize=10)
        elif T2 < 0:
            label = 'Maximum'
            if label not in legend_labels:
                ax.plot([ax_val], [ay_val], [T3], 'g+', markersize=10, label=label)
                legend_labels.append(label)
            else:
                ax.plot([ax_val], [ay_val], [T3], 'g+', markersize=10)
        else:
            label = 'Minimum'
            if label not in legend_labels:
                ax.plot([ax_val], [ay_val], [T3], 'r*', markersize=10, label=label)
                legend_labels.append(label)
            else:
                ax.plot([ax_val], [ay_val], [T3], 'r*', markersize=10)

    # Labeling and legend
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Display the legend only if any labels are present
    if legend_labels:
        ax.legend(loc='best')

    plt.show()
