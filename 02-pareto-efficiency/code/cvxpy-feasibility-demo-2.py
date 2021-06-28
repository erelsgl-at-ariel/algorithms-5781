#!python3

"""
A demo of cvxpy - the convex-optimization package of python.
"""


import cvxpy

# u1(A2) + 2 u1(t*) <=u1(A1) < u1(A2) + u1(t*)
# u2(A1)                <= u2(A2) < u2(A1) - r u1(t*)
# u2(A1) + r*u2(A2)  <= r*u1(A1) + u1(A2)

r = 1

u1A1 = cvxpy.Variable()
u1A2 = cvxpy.Variable()
u2A1 = cvxpy.Variable()
u2A2 = cvxpy.Variable()

u1t = cvxpy.Variable()
u2t = r*u1t

u1A1before =  u1A1 - u1t
u1A2before =  u1A2 + u1t
u2A1before =  u2A1 - u2t
u2A2before =  u2A2 + u2t


violation = cvxpy.Variable()

prob = cvxpy.Problem(cvxpy.Maximize(1), 
    constraints = [
        u1A1before >= u1A2before,        # 1 does not envy before tranfer
        u1A1 - u1t <= u1A2 - violation,  # 1 strong envies after tranfer
        u2A2 >= u2A1,                    # 2 does not envy after tranfer
        u2A2before - u2t <= u2A1before - violation,  # 2 strong envies before transfer
        # For all items x in A1:
        #     u2(x)/u1(x) >= r
        #     u2(x) <= r * u1(x)
        u2A1 <= r*u1A1,
        # For all items x in A2:
        #     u2(x)/u1(x) <= r
        #     u2(x) >= r * u1(x)
        u2A2 >= r*u1A2,
        u1A1 <= 0,
        u1A2 <= 0,
        u2A1 <= 0,
        u2A2 <= 0,
        u1A1before <= 0,
        u1A2before <= 0,
        u2A1before <= 0,
        u2A2before <= 0,
        u1t <= 0,
        violation >= 0.01,
        # u1A1 == -3,
        # u1A2 == -0.5,
        # u2A1 == -1.5,
        # u2A2 == -1.5,
        # u1t == -6,
    ]
    )
prob.solve()
print("status:", prob.status)
if prob.status=="optimal":
    print(f"u1A1={u1A1.value:.2}, u1A2={u1A2.value:.2}, u2A1={u2A1.value:.2}, u2A2={u2A2.value:.2}, u1t={u1t.value:.2}, u2t={u2t.value:.2}, violation={violation.value:.2}")
    print(f"Values before transfer (t* is in A2):")
    print(f"   Agent 1: for 1: {u1A1before.value:.2}, for 2: {u1A2before.value:.2}")
    print(f"   Agent 2: for 1: {u2A1before.value:.2}, for 2: {u2A2before.value:.2}")
    print(f"Values after transfer (t* is in A1):")
    print(f"   Agent 1: for 1: {u1A1.value:.2}, for 2: {u1A2.value:.2}")
    print(f"   Agent 2: for 1: {u2A1.value:.2}, for 2: {u2A2.value:.2}")

