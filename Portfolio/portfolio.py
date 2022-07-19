'''
model

decision variable(unknown)
objective
constraints
coefficient
'''


'''
decision variable:
weight

coefficient:
variance, covariance, return(mean), expective return(0.001)
'''
from gurobipy import*
import pandas as pd
import copy
import numpy as np

wb = pd.read_excel("../Naive_S_P500.xlsx" , sheet_name=None)
ret = copy.deepcopy(wb["return"].drop(columns=["Unnamed: 0"]))
assets_obs = ret.iloc[:100, 1:397]
n = assets_obs.shape[1]

"""
P = [1 * n]
w = [1 * n]
C = [n * n]
"""
P = np.asmatrix(np.mean(assets_obs, axis=0))
w = np.asmatrix(np.random.dirichlet(np.ones(n),size=1))
C = np.cov(assets_obs.T)


# init model
m = Model('mip1')
m.params.NonConvex = 2

# add decision variable
w = [m.addVar(lb=0.0) for x in range(n)]

# Update
m.update()

# objective
for i in range(n):
    m.setObjective(w[i] ** 2 * C.item(i, i) ** 2, GRB.MINIMIZE)
    for j in range(n):
        if i != j:
            m.setObjective(C.item(i, j) * w[i] * w[j], GRB.MINIMIZE)

# constraints
m.addConstr(quicksum([P.item(i)*w[i] for i in range(n)]) >= 0.001)
m.addConstr(quicksum(w) == 1)

# optimize
m.optimize()

# get variable name and value, get the objective result
for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
print('Obj: %g' % m.objVal)