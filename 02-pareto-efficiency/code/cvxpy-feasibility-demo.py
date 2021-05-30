#!python3

"""
A demo of cvxpy - the convex-optimization package of python.
"""

import cvxpy

# Create two scalar optimization variables.
x = cvxpy.Variable()
y = cvxpy.Variable()

prob = cvxpy.Problem(cvxpy.Minimize(1), 
    constraints = [x+y >= 1, x-y <= 1]
    )
prob.solve()
print("status:", prob.status)
if prob.status=="optimal":
    print(f"x={x.value}, y={y.value}")

