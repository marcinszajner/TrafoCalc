# TrafoCalc

Requirements
Python 3.8.5 <

Calculator should work on linux and windowsm
however FEMM not work on linux yet. 

How to use

1. Clone repository and run cmd in TrafoCalc folder.
2. check python by type in cmd "python -- version", if it is 3.8.5
or better continue
    - if python command is not finded, install python
3. type "python main.py" to run window with app
4. In upper left corner pres "load" and choose example.json file
5. From upper right list choose between:
    - Inductance - There are used "Inductor params" and create draw with gap.
    It use space for bobbin and insulator layer for simplify model
    - Electrostatic field simulation - It use Transformer input data. Draw only one side window wires
    with bobbin and insulator layer
    - Magnetic field simulation - It use Transformer input data. Create draw without gap.
    It use space for bobbin and insulator layer for simplify model
6. Press Run for precalculate transformer or inductor
7. Press "Create FEMM model" for create .FEM file (Magnetic)
 or .FEE (electrostatic)
8. Load created file by FEMM

![Screenshot](image/example_inductor.png)
Example output of inductor model in FEMM

![Screenshot](image/window_example.png)
Main window with loaded example