from pulp import *
import time


# Step 1: Creating an instance of an LP problem 
problem = LpProblem('Tesla_Factory', LpMaximize) 
# Step 2: Creating decision variables
U = LpVariable('Model_U', lowBound=0 , cat=LpInteger)
Z = LpVariable('Model_Z', lowBound=0 , cat=LpInteger)  
# Step 3: Specifying objective function and constraints
problem += 20000*U + 45000*Z , 'Objective Function' 
#Constraints
problem += 4*U + 5*Z <= 30, 'Designer Constraint'
problem += 3*U + 6*Z <=30, 'Engineer Constraint'
problem += 2*U + 7*Z <=30, 'Machine Constraint'
print("Current Status: ", LpStatus[problem.status])
# Solving the problem
problem.solve(PULP_CBC_CMD(msg=False))
print("Current Status: ", LpStatus[problem.status])
print("Number of Model U Made: ", U.varValue)
print("Number of Model Z Made: ", Z.varValue)
print("Total Profit: ", value(problem.objective)) 
