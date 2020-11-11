#!python3

"""
Using cvxpy - the convex optimization package of Python -
to find an egalitarian division.

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
x1, x2, x3 = cvxpy.Variable(), cvxpy.Variable(), cvxpy.Variable()

print("\nEgalitarian division")
# attempt 1:
# prob = cvxpy.Problem(
#     cvxpy.Maximize(min(81*x + 19, 80*(1-x)+20)),
#     constraints = [0 <= x, x <= 1])
# attempt 2:
z = cvxpy.Variable()
prob = cvxpy.Problem(
    cvxpy.Maximize(z),
    constraints = [0 <= x1, x1 <= 1, 0 <= x2, x2 <= 1, 0 <= x3, x3 <= 1,
                   19*x1 + 0*x2 + 81*x3 >= z, 0*(1-x1) + 20*(1-x2) + 80*(1-x3) >= z])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x1.value, x2.value, x3.value)
print("value of Ami", 19*x1.value + 0*x2.value + 81*x3.value)
print("value of Tami", 0*(1-x1.value) + 20*(1-x2.value) + 80*(1-x3.value))
#
# x.value = 0.5
# print("other x", x.value)
# print("value of Ami", 81*x.value+19)
# print("value of Tami", 80*(1-x.value)+20)
