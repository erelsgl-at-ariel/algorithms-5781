#!python3

"""
Using cvxpy - the convex optimization package of Python -
to find a fair and efficient division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

import cvxpy
from cvxpy import min

print("\n\n\nPROBLEM #1")
print("A cake with three regions has to be divided among two people with values:")
print("19 0 81")
print("0 20 80")

# Define x = the fraction of the third region given to the first agent.
x = cvxpy.Variable()

print("\nEgalitarian division")
# attempt 1:
# prob = cvxpy.Problem(
#     cvxpy.Maximize(min(81*x + 19, 80*(1-x)+20)),
#     constraints = [0 <= x, x <= 1])
# attempt 2:
z = cvxpy.Variable()
prob = cvxpy.Problem(
    cvxpy.Maximize(z),
    constraints = [0 <= x, x <= 1,
                   81*x + 19 >= z, 80*(1-x)+20 >= z])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)
print("value of Ami", 81*x.value+19)
print("value of Tami", 80*(1-x.value)+20)

