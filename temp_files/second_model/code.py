

import pandas as pd
import libsbml
import petab
import yaml
import os
import benchmark_models_petab as models
import numpy as np
import pypesto
import pypesto.petab
import matplotlib.pyplot as plt
import pypesto.optimize as optimize
import pypesto.visualize as visualize
from pypesto.visualize.model_fit import visualize_optimized_model_fit





# pandas's dataframes for the first model(EGF as stimuli)
experimental_condition = pd.DataFrame({
    'conditionId': ['EGF_stimuli']   
})



measurement = pd.DataFrame({
    'observableId': ['EGF_1', 'pErk_1', 'pErk_1', 'pErk_1', 'pErk_1',
                     'pErk_1', 'pErk_1', 'pErk_1', 'pErk_1', 'pErk_1'],
    'simulationConditionId': ['EGF_stimuli','EGF_stimuli','EGF_stimuli','EGF_stimuli',
                              'EGF_stimuli','EGF_stimuli','EGF_stimuli','EGF_stimuli',
                              'EGF_stimuli','EGF_stimuli'],
    'measurement': [100,0.01,0.7,1,0.41,0.1,0.03,0.01,0.01,0.01],
    'time': [0.01, 0.01, 100, 280, 420, 600, 840, 1800, 2400, 3000]
})


observables = pd.DataFrame({
    'observableId': ['EGF_1','Raf_1', 'pRaf_1', 'Mek_1', 'pMek_1', 'Erk_1', 'pErk_1'],
    'observableFormula': ['-r0*EGF*Raf', '(r_1*pMek*pRaf)+(r_3*pErk*pRaf)-(r0*EGF*Raf)',
                          '(r0*EGF*Raf)-(r_1*pMek*pRaf)-(r3*pRaf*Erk)-(r_3*pErk*pRaf)',
                          '(r_2*pErk*pMek)-(r1*pRaf*Mek)',
                          '(r1*pRaf*Mek)-(r_1*pMek*pRaf)-(r2*pMek*Erk)-(r_2*pErk*pMek)',
                          '(r4*pErk)-(r3*pRaf*Erk)-(r2*pMek*Erk)',
                          '(r2*pMek*Erk)-(r_2*pErk*pMek)+(r3*pRaf*Erk)-(r_3*pErk*pRaf)-(r4*pErk)'
                         ],
    'noiseFormula': ['sigma', 'sigma' , 'sigma', 'sigma', 'sigma' , 'sigma', 'sigma'],
    'noiseDistribution': ['normal','normal','normal','normal','normal','normal','normal']
})




parameter = pd.DataFrame({
    'parameterId':    ['r0', 'r1', 'r2', 'r3', 'r_1', 'r_2', 'r_3','r4','sigma'],
    'parameterScale':   ['lin','lin','lin','lin','lin','lin','lin','lin','lin'],
    'lowerBound': [0, 0.78, 0.88, -0.02, -0.37, -0.79, -0.88, 0, 0.001],
    'upperBound': [5,  1.52, 1.10,  0.21,  0.12, -0.07, -0.32,  5,  0.01],
    'nominalValue': [None,1.11, 1.08,  0.09,  -0.10,-0.35, -0.53,  None,  None],
    'estimate':     [1, 0, 0, 0, 0, 0, 0, 1, 1]
})




visualization =pd.DataFrame({
    'plotId': ['plot_1'],
    'plotTypeData': ['MeanAndSD'],
    'xLabel': ['Time(second)'],
    'yValues': ['pErk_1'],
    'yLabel' : ['ppErk']  
})






# The directories where the data will be stored

file_path_egf_1 = "/home/loqman/petab_files(1)/egf3/parameter.tsv"
file_path_egf_2 = "/home/loqman/petab_files(1)/egf3/experimental_condition.tsv"
file_path_egf_3 = "/home/loqman/petab_files(1)/egf3/observables.tsv"
file_path_egf_4 = "/home/loqman/petab_files(1)/egf3/measurement.tsv"
file_path_egf_5 = "/home/loqman/petab_files(1)/egf3/visualization.tsv"





# Convert pandas dataframes to tsv files with tab separator

parameter.to_csv(file_path_egf_1,   sep='\t',  index=False)
experimental_condition.to_csv(file_path_egf_2,  sep='\t',index=False)
observables.to_csv(file_path_egf_3,  sep='\t', index=False)
measurement.to_csv(file_path_egf_4,  sep='\t', index=False)
visualization.to_csv(file_path_egf_5, sep='\t',index=False)





"""

The SBML files were generated using the https://sys-bio.github.io/makesbml/ tool.

EGF:
# Reactions

R1: EGF + Raf -> pRaf;  r0 * EGF * Raf
R2: pRaf + Mek -> pMek; r1 * pRaf * Mek
R3: pMek + pRaf -> Raf; r_1 * pMek * pRaf
R4: pMek + Erk -> pErk; r2 * pMek * Erk
R5: pErk + pMek -> Mek; r_2 * pErk * pMek
R6: pRaf + Erk -> pErk; r3 * pRaf * Erk
R7: pErk + pRaf -> Raf; r_3 * pErk * pRaf
R8: pErk -> Erk ; r4 * pErk 

# initial concentrations

EGF = 100
Raf = 1
Mek = 1
Erk = 1
pRaf = 0
pMek = 0
pErk = 0

# rate constants

r0 = 1
r1 = 1.11
r2 = 1
r3 = 0.09
r_1 = 0.1
r_2 = 0.57
r_3 = 0.25
r4 = 1
sigma = 1  
"""





measurement_egf =  "/home/loqman/petab_files(1)/egf/measurement.tsv"
visualization_egf =  "/home/loqman/petab_files(1)/egf/visualization.tsv"
sbml_egf_file = "/home/loqman/petab_files(1)/egf3/egf_model.xml"
condition_egf_file = "/home/loqman/petab_files(1)/egf3/experimental_condition.tsv"
observable_egf_file = "/home/loqman/petab_files(1)/egf3/observables.tsv"
parameter_egf_file = "/home/loqman/petab_files(1)/egf3/parameter.tsv"
measurement_egf_file = "/home/loqman/petab_files(1)/egf3/measurement.tsv"
visualization_egf_file = "/home/loqman/petab_files(1)/egf3/visualization.tsv"


# Specify the output directory for the YAML file
output_directory = "/home/loqman/petab_files(1)/egf3/"



# Create petab problem
petab_problem_egf = petab.Problem()
petab_problem_egf.sbml_file = [sbml_egf_file]
petab_problem_egf.condition_file = [condition_egf_file]
petab_problem_egf.observable_file = [observable_egf_file]
petab_problem_egf.parameter_file = [parameter_egf_file]
petab_problem_egf.measurement_file = [measurement_egf_file]
petab_problem_egf.visualization_file = [visualization_egf_file]





# Create a dictionary to store the PEtab configuration
petab_config_egf = {
    'format_version': '1.0.0',
    'parameter_file': [parameter_egf_file],  
    'problems': [
        {
            'condition_files': [condition_egf_file],  
            'measurement_files': [measurement_egf_file],  
            'sbml_files': [sbml_egf_file],  
            'observable_files': [observable_egf_file],  
            'visualization_files': [visualization_egf_file],  
        }
    ]
}





# Specify the output YAML file paths
yaml_egf_path = output_directory + "egf3_model.yaml"

# Write the PEtab configurations to YAML files
with open(yaml_egf_path, "w") as yaml_file:
    yaml.dump(petab_config_egf, yaml_file, default_flow_style=False)


# In[95]:


# Specify the paths to your existing YAML files
yaml_egf_path = "/home/loqman/petab_files(1)/egf3/egf3_model.yaml"

# Load the existing YAML files to create petab problems
petab_problem_egf = petab.Problem.from_yaml(yaml_egf_path)


# In[96]:


egf_importer = pypesto.petab.PetabImporter(petab_problem_egf)


egf_model = egf_importer.create_model()


print("EGF_Model parameters:", list(egf_model.getParameterIds()), "\n")
print("EGF_Model const parameters:", list(egf_model.getFixedParameterIds()), "\n")
print("EGF_Model outputs: ", list(egf_model.getObservableIds()), "\n")
print("EGF_Model states: ", list(egf_model.getStateIds()), "\n")

"""
outputs:

EGF_Model parameters: ['r0', 'd', 'sigma'] 

EGF_Model const parameters: ['r1', 'r_1', 'r2', 'r_2', 'r3', 'r_3'] 

EGF_Model outputs:  ['EGF_1', 'Raf_1', 'Mek_1', 'Erk_1'] 

EGF_Model states:  ['EGF', 'Raf', 'Mek', 'Erk'] 

why it should return d !!!

"""





# To perform parameter estimation, we need to define an objective function.

egf_converter_config = libsbml.SBMLLocalParameterConverter().getDefaultProperties()
petab_problem_egf.sbml_document.convert(egf_converter_config)

egf_obj = egf_importer.create_objective()


egf_ret = egf_obj(
    petab_problem_egf.x_nominal_scaled,
    mode="mode_fun",
    sensi_orders=(0, 1),
    return_dict=True,
)
print(egf_ret)





# The problem defined in PEtab also defines the fixed parameters and parameter bounds.
# This information is contained in a pypesto.Problem.
egf_problem = egf_importer.create_problem(egf_obj)
print(egf_problem.x_fixed_indices, egf_problem.x_free_indices)

egf_objective = egf_problem.objective
egf_ret = egf_objective(petab_problem_egf.x_nominal_free_scaled, sensi_orders=(0, 1))
print(egf_ret)





egf_eps = 1e-4


def egf_fd(x):
    grad = np.zeros_like(x)
    j = 0
    for i, xi in enumerate(x):
        mask = np.zeros_like(x)
        mask[i] += egf_eps
        valinc, _ = egf_objective(x + mask, sensi_orders=(0, 1))
        valdec, _ = egf_objective(x - mask, sensi_orders=(0, 1))
        grad[j] = (valinc - valdec) / (2 * egf_eps)
        j += 1
    return grad


egf_fdval = egf_fd(petab_problem_egf.x_nominal_free_scaled)
print("egf_fd: ", egf_fdval)
print("l2 difference: ", np.linalg.norm(egf_ret[1] - egf_fdval))





egf_optimizer = optimize.ScipyOptimizer()

# engine = pypesto.engine.SingleCoreEngine()
egf_engine = pypesto.engine.MultiProcessEngine()

# do the optimization
egf_result = optimize.minimize(problem=egf_problem,
                               optimizer=egf_optimizer, n_starts=10, engine=egf_engine)

egf_result.optimize_result.fval





# the standard pypesto plotting
egf_ref = visualize.create_references(x=petab_problem_egf.x_nominal_scaled,
                                      fval=egf_obj(petab_problem_egf.x_nominal_scaled))

visualize.waterfall(egf_result, reference=egf_ref, scale_y="lin")
visualize.parameters(egf_result, reference=egf_ref)





# visualize the model fit
visualize_optimized_model_fit(petab_problem=petab_problem_egf,
                              result=egf_result, pypesto_problem=egf_problem)

