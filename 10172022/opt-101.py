## code adapted from https://medium.com/opex-analytics/optimization-modeling-in-python-pulp-gurobi-and-cplex-83a62129807a
import random
import gurobipy as grb
n = 10
m = 5
set_I = range(1,n+1)
set_J = range(1,m+1)
c = {(i,j):random.normalvariate(0,1) for i in set_I for j in set_J}
a = {(i,j):random.normalvariate(0,5) for i in set_I for j in set_J}
l = {(i,j):random.normalvariate(0,10) for i in set_I for j in set_J}
u = {(i,j):random.normalvariate(10,20) for i in set_I for j in set_J}
b = {j:random.randint(0,30) for j in set_J}


opt_model = grb.Model(name = 'MIP Model')

x_vars = {(i,j):opt_model.addVar(vtype = grb.GRB.CONTINUOUS,lb = l[i,j],ub = u[i,j],name = "x_{0}_{1}".format(i,j)) for i in set_I for j in set_J}

constraints = {j: opt_model.addLConstr(lhs = grb.quicksum(a[i,j]*x_vars[i,j] for i in set_I),
                                      sense = grb.GRB.LESS_EQUAL,rhs = b[j],name = "constraint_{0}".format(j)) for j in set_J
                                      }
objective = grb.quicksum(c[i,j]*x_vars[i,j] for i in set_I for j in set_J)
opt_model.ModelSense = grb.GRB.MAXIMIZE  
opt_model.optimize()                                   