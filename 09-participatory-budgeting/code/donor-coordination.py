#!python3

"""
Demonstration of the donor coordination algorithm maximizing the product of utilities.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""


from itertools import chain, combinations
import cvxpy
import functools

# There are 4 projects, denoted by a, b, c, d.
# The same letters denote the budget allocated to them.
allocations = cvxpy.Variable(4)
a, b, c, d = allocations

# There are 5 citizens. Their preferences are: ab, ac, ad, bc, a. Their donations are 100 each.
donations = [100, 100, 100, 100, 100]
utilities = [a+b, a+c, a+d, b+c, a]

sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])
positivity_constraints = [v>=0 for v in allocations]
sum_constraint = [cvxpy.sum(allocations)==sum(donations)]

problem = cvxpy.Problem(
    cvxpy.Maximize(sum_of_logs),
    constraints = positivity_constraints+sum_constraint)
problem.solve()

utility_values = [u.value/100 for u in utilities]
print("BUDGET: a={}, b={}, c={}, d={}".format(a.value, b.value, c.value, d.value))
print("UTILS : {}, {}, {}, {}, {}".format(*utility_values))
utility_product = functools.reduce(lambda a,b: a*b, utility_values)
print("PRODUCT: {}".format(utility_product))
i=0
print("Citizen {} should donate {} to a and {} to b".format(i,
    a.value * donations[i] / utilities[i].value,
    b.value * donations[i] / utilities[i].value
))
i+=1
print("Citizen {} should donate {} to a and {} to c".format(i,
    a.value * donations[i] / utilities[i].value,
    c.value * donations[i] / utilities[i].value
))
i+=1
print("Citizen {} should donate {} to a and {} to d".format(i,
    a.value * donations[i] / utilities[i].value,
    d.value * donations[i] / utilities[i].value
))
i+=1
print("Citizen {} should donate {} to b and {} to c".format(i,
    b.value * donations[i] / utilities[i].value,
    c.value * donations[i] / utilities[i].value
))
i+=1
print("Citizen {} should donate {} to a".format(i,
    a.value * donations[i] / utilities[i].value,
))
