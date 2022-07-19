import gurobipy as gp
from gurobipy import GRB, quicksum
import pandas as pd
import copy
import numpy as np

df = pd.read_excel('../Naive_S_P500.xlsx', sheet_name='return')
ret = copy.deepcopy(df.drop(columns=['Unnamed: 0']))
ret = ret.iloc[:5, 1:397]
n = [i for i in range(396)]

cov = ret.cov()
var = ret.var()
mean = ret.mean()

m = gp.Model('MV_model')
m.params.NonConvex = 2

w = [m.addVar(lb=0.0, ub=1.0) for i in n]
m.update()

eq1 = quicksum(w[i]**2 * var.iloc[i] for i in n) + quicksum([cov.iloc[i, j] * w[i] * w[j] for i in n for j in n if i != j])
m.setObjective(eq1, GRB.MINIMIZE)
eq2 = quicksum(mean.iloc[i] * w[i] for i in n)
eq3 = quicksum(w[i] for i in n)
m.addConstr(eq2 >= 0.001)
m.addConstr(eq3 == 1)

m.optimize()
for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
print('Obj: %g' % m.objVal)