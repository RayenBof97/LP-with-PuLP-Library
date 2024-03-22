from pulp import *

# Step 1: Creating an instance of an LP problem 
problem = LpProblem('Industrie_Textile', LpMaximize) 
# Step 2: Creating decision variables
X = LpVariable('Nombre Produit 1', lowBound=0 , cat=LpInteger)
Y = LpVariable('Nombre Produit 2', lowBound=0 , cat=LpInteger)  
Z = LpVariable('Nombre Produit 3', lowBound=0 , cat=LpInteger)  
# Step 3: Specifying objective function and constraints
problem += 7*X + 10*Y + 12*Z , 'Objective Function : Maximisation de profit' 
#Constraints
problem += 3*X + 2*Y + 4*Z <=120, 'Contrainte Machine 1'
problem += 8*X + 7*Y + 4*Z <=150, 'Contrainte Machine 2'
problem += 0.7*X + 0.6*Y + 0.3*Z <=100, 'Contrainte Machine 3'
print("Current Status: ", LpStatus[problem.status])
# Solving the problem
problem.solve(PULP_CBC_CMD(msg=False))
print("Current Status: ", LpStatus[problem.status])
print("Nombre de Produit 1 optimal : ", X.varValue)
print("Nombre de Produit 2 optimal : ", Y.varValue)
print("Nombre de Produit 3 optimal : ", Z.varValue)
print("Profit: ", value(problem.objective)) 
