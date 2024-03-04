# Truss (Two-Force Members) Problem Solver

## Purpose

This Python script generates a global stiffness matrix, a force vector, a displacement vector, and stress analysis of bars (identifying tension and compression) for any type of truss-related problem. It takes user input for the number of nodes, the number of elements, which nodes have forces applied, and the initial and final coordinates of each truss bar, among other parameters.

## Code Description

The code performs the following steps:

1. **Initialize Variables:** Initialize variables for the number of elements (`e`), the number of nodes (`n`), arrays for the global stiffness matrix (`K`), the force vector (`f`), and others.
2. **Get Element Information:** Prompt the user to input information about each truss element, including initial and final node numbers, initial and final coordinates, area, and elastic modulus.
3. **Assemble Stiffness Matrix:** Assemble the global stiffness matrix based on user input for each truss element.
4. **Get Node Forces:** Prompt the user to input force values for each node.
5. **Define Supports:** Prompt the user to input the number of fixed degrees of freedom and specify which nodes are supported.
6. **Solve for Displacement and Reaction Forces:** Solve the system of equations to determine the displacement vector (`U`) and reaction forces vector (`F`).
7. **Stress Analysis:** Calculate the stress of each truss element and identify if it's in tension or compression.
8. **Print Results:** Display the global stiffness matrix, force vector, displacement vector, reaction forces, and stress analysis results.

## Requirements

- Python 3.x
- Required Python packages: numpy, calfem

## Usage

1. Ensure Python 3.x is installed on your system.
2. Install required Python packages using pip:
3. Copy the provided code into a Python script (e.g., `truss_problem_solver.py`).
4. Run the Python script:
5. Follow the on-screen instructions to input the necessary parameters and obtain the results.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
