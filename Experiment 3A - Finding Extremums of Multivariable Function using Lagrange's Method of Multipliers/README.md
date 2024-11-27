# Aim
Finding the Maxima and Minima of a function f(x,y) = x^2 + y^2 subject to g(x,y) = x + y - 10 by using Lagrange's Method of Multipliers.

# Output
```
Stationary point: x = 5.000000000000001, y = 5.000000000000001
Function value at stationary point: f(x, y) = 50.00000000000002
```
![matlab-code-python-rewrite](https://github.com/felixity1917/matlab-code-python-rewrite/blob/main/Experiment%203A%20-%20Finding%20Extremums%20of%20Multivariable%20Function%20using%20Lagrange's%20Method%20of%20Multipliers/Assets/Figure_1.png?raw=true)

# Note
main_2.py contains code adjusted to when the constraint is x * y - 5. I have been unable to get the graph to show up properly so it is WIP for the time being. The error arises when `gv_y = 5 / gv_x` is assigned, key-point being the division part.
