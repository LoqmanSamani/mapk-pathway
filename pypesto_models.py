#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import amici
import benchmark_models_petab as models
import matplotlib.pyplot as plt
import numpy as np
import petab
import pypesto
import pypesto.optimize as optimize
import pypesto.petab
import pypesto.visualize as visualize



# Specify the paths to the existing YAML files (you can find the code to prepare petab
# files in 'prepared_files_for_a_pypesto_analysis.py')
yaml_egf_path = "/home/loqman/petab_files(1)/egf/egf_model.yaml"
yaml_ngf_path = "/home/loqman/petab_files(1)/ngf/ngf_model.yaml"



# Load the existing YAML files to create petab problems
petab_problem_egf = petab.Problem.from_yaml(yaml_egf_path)
petab_problem_ngf = petab.Problem.from_yaml(yaml_ngf_path)


importer1 = pypesto.petab.PetabImporter(petab_problem_egf)
importer2 = pypesto.petab.PetabImporter(petab_problem_ngf)


model1 = importer1.create_model()
model2 = importer2.create_model()


# When running the code, the error below appears! I am working on it!
"""
Compiling amici model to folder /home/loqman/amici_models/tmp48nwpiod.
2023-09-13 16:07:44.944 - amici.petab_import - INFO - Compiling model tmp48nwpiod to /home/loqman/amici_models/tmp48nwpiod.
2023-09-13 16:07:44.949 - amici.petab_import - INFO - Importing model ...
2023-09-13 16:07:44.950 - amici.petab_import - INFO - Validating PEtab problem ...
2023-09-13 16:07:44.974 - amici.petab_import - INFO - Model name is 'tmp48nwpiod'.
Writing model code to '/home/loqman/amici_models/tmp48nwpiod'.
2023-09-13 16:07:44.975 - amici.petab_import - INFO - Species: 0
2023-09-13 16:07:44.975 - amici.petab_import - INFO - Global parameters: 0
2023-09-13 16:07:44.975 - amici.petab_import - INFO - Reactions: 8
2023-09-13 16:07:44.995 - amici.sbml_import - ERROR - libSBML SBML component consistency (Error): A <reaction> definition must contain at least one <speciesReference>, either in its <listOfReactants> or its <listOfProducts>. A reaction without any reactant or product species is not permitted, regardless of whether the reaction has any modifier species.
Reference: L3V1 Section 4.11.3
 The <reaction> with id 'R1' does not contain any reactants or products. 

2023-09-13 16:07:44.995 - amici.sbml_import - ERROR - libSBML SBML component consistency (Error): A <reaction> definition must contain at least one <speciesReference>, either in its <listOfReactants> or its <listOfProducts>. A reaction without any reactant or product species is not permitted, regardless of whether the reaction has any modifier species.
Reference: L3V1 Section 4.11.3
 The <reaction> with id 'R2' does not contain any reactants or products. 

2023-09-13 16:07:44.995 - amici.sbml_import - ERROR - libSBML SBML component consistency (Error): A <reaction> definition must contain at least one <speciesReference>, either in its <listOfReactants> or its <listOfProducts>. A reaction without any reactant or product species is not permitted, regardless of whether the reaction has any modifier species.
Reference: L3V1 Section 4.11.3
 The <reaction> with id 'R3' does not contain any reactants or products. 

2023-09-13 16:07:44.996 - amici.sbml_import - ERROR - libSBML SBML component consistency (Error): A <reaction> definition must contain at least one <speciesReference>, either in its <listOfReactants> or its <listOfProducts>. A reaction without any reactant or product species is not permitted, regardless of whether the reaction has any modifier species.
Reference: L3V1 Section 4.11.3
 The <reaction> with id 'R4' does not contain any reactants or products. 

2023-09-13 16:07:44.996 - amici.sbml_import - ERROR - libSBML SBML component consistency (Error): A <reaction> definition must contain at least one <speciesReference>, either in its <listOfReactants> or its <listOfProducts>. A reaction without any reactant or product species is not permitted, regardless of whether the reaction has any modifier species.
Reference: L3V1 Section 4.11.3
 The <reaction> with id 'R5' does not contain any reactants or products. 

2023-09-13 16:07:44.997 - amici.sbml_import - ERROR - libSBML SBML component consistency (Error): A <reaction> definition must contain at least one <speciesReference>, either in its <listOfReactants> or its <listOfProducts>. A reaction without any reactant or product species is not permitted, regardless of whether the reaction has any modifier species.
Reference: L3V1 Section 4.11.3
 The <reaction> with id 'R6' does not contain any reactants or products. 

2023-09-13 16:07:44.997 - amici.sbml_import - ERROR - libSBML SBML component consistency (Error): A <reaction> definition must contain at least one <speciesReference>, either in its <listOfReactants> or its <listOfProducts>. A reaction without any reactant or product species is not permitted, regardless of whether the reaction has any modifier species.
Reference: L3V1 Section 4.11.3
 The <reaction> with id 'R7' does not contain any reactants or products. 

2023-09-13 16:07:44.998 - amici.sbml_import - ERROR - libSBML SBML component consistency (Error): A <reaction> definition must contain at least one <speciesReference>, either in its <listOfReactants> or its <listOfProducts>. A reaction without any reactant or product species is not permitted, regardless of whether the reaction has any modifier species.
Reference: L3V1 Section 4.11.3
 The <reaction> with id 'R8' does not contain any reactants or products. 

"""


