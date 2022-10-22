import gurobipy as grb
opt_model = grb.Model(name = 'MIP Model')
xa = opt_model.addVar(vtype=grb.GRB.INTEGER,lb=0,ub=1,name="xa")
xb = opt_model.addVar(vtype=grb.GRB.INTEGER,lb=0,ub=1,name="xb")
xc = opt_model.addVar(vtype=grb.GRB.INTEGER,lb=0,ub=1,name="xc")
xd = opt_model.addVar(vtype=grb.GRB.INTEGER,lb=0,ub=1,name="xd")
opt_model.addLConstr(lhs=(xa+xb+xd),sense=grb.GRB.LESS_EQUAL,rhs=1, name="c1")
opt_model.addLConstr(lhs=(xa+xb+xc),sense=grb.GRB.LESS_EQUAL,rhs=1, name="c2")
opt_model.addLConstr(lhs=(xb+xc),sense=grb.GRB.LESS_EQUAL,rhs=1, name="c3")
opt_model.addLConstr(lhs=(xa+xd),sense=grb.GRB.LESS_EQUAL,rhs=1, name="c4")
opt_model.addLConstr(lhs=(xa+xb+xc),sense=grb.GRB.LESS_EQUAL,rhs=1, name="c5")
opt_model.addLConstr(lhs=(xb+xd),sense=grb.GRB.LESS_EQUAL,rhs=1, name="c6")
objective = 320*xa+320*xb+140*xc+330*xd
opt_model.ModelSense = grb.GRB.MAXIMIZE
opt_model.setObjective(objective)
opt_model.optimize()
print(opt_model.x)