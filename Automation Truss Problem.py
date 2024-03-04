!pip install calfem-python

import numpy as np
import calfem.core as cfc

e = int(input("Enter the number of Elements: "))
n = int(input("Enter the number of Nodes: "))
K = np.zeros((n, n))
f = np.zeros((n, 1))
Edof = np.zeros((e, 2), dtype=int)  # Initialize Edof array

# Getting input for node to node history
for i in range(e):
    val_1 = int(input(f"Enter initial node number of element {i + 1} = "))
    val_2 = int(input(f"Enter final node number of element {i + 1} = "))
    Edof[i] = [val_1, val_2]

# Assemble the K matrix based on user input
for i in range(e):
    stiffness_value = float(input(f"Enter stiffness value for element K{i + 1} as 'N/mm' = "))
    element_stiffness = cfc.spring1e(stiffness_value)
    cfc.assem(Edof[i], K, element_stiffness)

# Getting input for node Force history
for i in range(n):
    a = float(input(f"Enter node {i + 1} force as N = "))
    f[i] = a

b = int(input("Enter the number of supports = "))

bc = np.zeros(b, dtype=int)

for i in range(b):
    element = int(input(f"Enter support {i + 1} node number = "))
    bc[i] = element

U,F =cfc.solveq(K,f,bc)

print(f"\nGlobal Stiffness Matrix\n\n{K}\n\nForce Vector\n\n{f}\n\nDisplacement\n\n{np.around(U, decimals=3)}\n\nForce\n\n{np.around(F, decimals=3)}")