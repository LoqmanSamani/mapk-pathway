


import pandas as pd
import libsbml
import petab
import yaml
import os
import benchmark_models_petab as models
import numpy as np
import pypesto
import pypesto.petab


# Specify the paths to your existing YAML files
yaml_egf_path = "/home/loqman/petab_files(1)/egf/egf_model.yaml"
yaml_ngf_path = "/home/loqman/petab_files(1)/ngf/ngf_model.yaml"



# Load the existing YAML files to create petab problems
petab_problem_egf = petab.Problem.from_yaml(yaml_egf_path)
petab_problem_ngf = petab.Problem.from_yaml(yaml_ngf_path)


importer1 = pypesto.petab.PetabImporter(petab_problem_egf)
importer2 = pypesto.petab.PetabImporter(petab_problem_ngf)


model1 = importer1.create_model()
model2 = importer2.create_model()




# The current error

"""
Missing parameter(s) in the model or the parameters table: {'EGF_stimuli'}
Not OK

<IPython.core.display.Image object>

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[14], line 28
     25 petab_problem_ngf = petab.Problem.from_yaml(yaml_ngf_path)
     27 importer1 = pypesto.petab.PetabImporter(petab_problem_egf)
---> 28 importer2 = pypesto.petab.PetabImporter(petab_problem_ngf)
     30 model1 = importer1.create_model()
     31 model2 = importer2.create_model()

File ~/anaconda3/lib/python3.11/site-packages/pypesto/petab/importer.py:129, in PetabImporter.__init__(self, petab_problem, output_folder, model_name, validate_petab, validate_petab_hierarchical, hierarchical, inner_options)
    127 if validate_petab:
    128     if petab.lint_problem(petab_problem):
--> 129         raise ValueError("Invalid PEtab problem.")
    130 if self._hierarchical and validate_petab_hierarchical:
    131     from ..hierarchical.petab import (
    132         validate_hierarchical_petab_problem,
    133     )

ValueError: Invalid PEtab problem.


"""

# The problem is definitely in the tsv files, as the sbml file
# was created by "https://sys-bio.github.io/makesbml/". 
# If you add EGF_stimuli as a parameter to the parameter table,
# the error will be:


"""
Extraneous parameter(s) in parameter table: {'EGF_stimuli'}
{'EGF_stimuli'} is not allowed to occur in the parameters table.
Not OK

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[17], line 1
----> 1 importer1 = pypesto.petab.PetabImporter(petab_problem_egf)
      2 importer2 = pypesto.petab.PetabImporter(petab_problem_ngf)
      5 model1 = importer1.create_model()

File ~/anaconda3/lib/python3.11/site-packages/pypesto/petab/importer.py:129, in PetabImporter.__init__(self, petab_problem, output_folder, model_name, validate_petab, validate_petab_hierarchical, hierarchical, inner_options)
    127 if validate_petab:
    128     if petab.lint_problem(petab_problem):
--> 129         raise ValueError("Invalid PEtab problem.")
    130 if self._hierarchical and validate_petab_hierarchical:
    131     from ..hierarchical.petab import (
    132         validate_hierarchical_petab_problem,
    133     )

ValueError: Invalid PEtab problem.

"""
