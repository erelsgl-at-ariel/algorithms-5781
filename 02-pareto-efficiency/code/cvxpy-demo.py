#!python3

"""
A demo of cvxpy - the convex-optimization package of python.
"""

import cvxpy

# Create two scalar optimization variables.
x = cvxpy.Variable()
y = cvxpy.Variable()

# Create two constraints.
constraints = [x + y == 1,
               x - y >= 1]

# Form objective.
obj = cvxpy.Minimize((x - y)**2)

# Form and solve problem.
prob = cvxpy.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)
