import gurobipy as gp
from gurobipy import GRB

# Create a new model
m = gp.Model("cqm")

# Create variables
x = m.addVar(name="x", vtype=GRB.INTEGER)
y = m.addVar(name="y", vtype=GRB.INTEGER)
z = m.addVar(name="z", vtype=GRB.INTEGER)

# Set objective: x^2 + 2 y^2 - xz
obj = x ** 2 + 2 * y ** 2 - z * x
m.setObjective(obj, GRB.MINIMIZE)

# Add constraint: x + 2 y + 3 z <= 4
m.addConstr(x + 2 * y + 3 * z <= 4, "c0")

# Add constraint: x + y >= 1
m.addConstr(x + y >= 1, "c1")

m.optimize()

for v in m.getVars():
    print('%s %g' % (v.VarName, v.X))

print('Obj: %g' % obj.getValue())

m.write('test_problem.lp')
