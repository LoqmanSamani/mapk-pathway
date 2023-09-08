#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
The provided code generatesis the essential
files required for a Pypesto analysis, a framework used for parameter
estimation and optimization in systems biology. These files include 
the SBML model, parameter tables (in TSV format), experimental condition
tables, observable tables, and measurement tables.

"""


import pandas as pd
import libsbml
import petab
import yaml




# EGF Stimulation
parameters = pd.DataFrame({
    'parameterId': ['r0', 'r1', 'r2', 'r3', 'r_1', 'r_2', 'r_3'],
    'parameterScale': ['lin','lin','lin','lin','lin','lin','lin'],
    'lowerBound': [-5, 0.78, 0.88, -0.02, -0.37, -0.79, -0.88],
    'upperBound': [5, 1.52, 1.10, 0.21, 0.12, -0.07, -0.32],
    'nominalValue': [None, None, None, None, None, None, None],
    'estimate': [1, 1, 1, 1, 1, 1, 1]
})




ex_condition = pd.DataFrame({
    'conditionId': ['EGF_stimulation'],
    'conditionName': ['EGF_5_Minutes'],
    'Epo_concentration': ['1.25E-7']  
})



observation = pd.DataFrame({
    'observableId': ['EGF','Raf', 'Mek', 'Erk'],
    'observableName': ['Egf_stimuli','Raf_kinase','Mek_kinase','Erk_kinase'],
    'observableFormula': ['r0*EGF', 'r0*EGF + r_3*Erk + r1*Raf - r3*Raf',
                          'r1*Raf - r_2*Erk - r_1*Mek - r2*Mek',
                          'r3*Raf - r2*Mek - r_1*Erk - r_3*Erk'],
    'noiseFormula': [None, None, None, None],
    'noiseDistribution': [None, None, None, None]
})




measurement = pd.DataFrame({
    'observableId': ['EGF','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk'],
    'simulationConditionId': ['EGF_stimulation','EGF_stimulation','EGF_stimulation',
                              'EGF_stimulation','EGF_stimulation','EGF_stimulation',
                              'EGF_stimulation','EGF_stimulation','EGF_stimulation',
                              'EGF_stimulation',],
    'measurement': [100,0,0.7,1,0.41,0.1,0.03,0.01,0.01,0.01],
    'time': [0, 0, 100, 280, 420, 600, 840, 1800, 2400, 3000],
    'noiseParameters': [None, None, None, None, None, None, None, None, None, None]
})




visualization =pd.DataFrame({
    'plotId': ['plot_1'],
    'plotTypeData': ['MeanAndSD'],
    'xLabel': ['Time(sec)'],
    'yValues': ['Erk'],
    'yLabel' : ['ppERK']  
})



directory = '/home/PEtab_files/' # path

file_name1 = 'parameters.tsv'
file_name2 = 'ex_condition.tsv'
file_name3 = 'observation.tsv'
file_name4 = 'measurement.tsv'
file_name5 = 'visualization.tsv'


file_path1 = directory + file_name1
file_path2 = directory + file_name2
file_path3 = directory + file_name3
file_path4 = directory + file_name4
file_path5 = directory + file_name5


parameters.to_csv(file_path1, sep='\t', index=False)
ex_condition.to_csv(file_path2, sep='\t', index=False)
observation.to_csv(file_path3, sep='\t', index=False)
measurement.to_csv(file_path4, sep='\t', index=False)
visualization.to_csv(file_path5, sep='\t', index=False)



sbml_file = pd.DataFrame({
    'ID': ['R1', 'R2', 'R3', 'R4', 'R5','R6','R7'],
    'Reaction': ['EGF->Raf','Raf->Mek','Mek->Raf',
                 'Mek->Erk','Erk->Mek','Raf->Erk','Erk->Raf'],
    'Rate law': ['r0 * EGF','r1 * Raf','r_1 * Mek','r2 * Mek',
                 'r_2 * Erk','r3 * Raf','r_3 * Erk']
})


doc = libsbml.SBMLDocument(3, 1)
model = doc.createModel()

for index, row in sbml_file.iterrows():
   
    reaction = model.createReaction()
    reaction.setId(row['ID'])
    reaction.setName(row['Reaction'])
    
   
    kinetic_law = libsbml.KineticLaw(3, 1) 
    kinetic_law.setMath(libsbml.parseL3Formula(row['Rate law']))
    reaction.setKineticLaw(kinetic_law)


sbml_file_path = "/home/PEtab_files/model.sbml"
libsbml.writeSBMLToFile(doc, sbml_file_path)



# Define paths to your SBML and TSV files
sbml_file_path = "/home/PEtab_files/model.sbml"
conditions_tsv_path = "/home/PEtab_files/ex_condition.tsv"
observables_tsv_path = "/home/PEtab_files/observation.tsv"
parameters_tsv_path = "/home/PEtab_files/parameters.tsv"
measurements_tsv_path = "/home/PEtab_files/measurement.tsv"
visualization_tsv_path = "/home/PEtab_files/visualization.tsv"


petab_problem = petab.Problem()


petab_problem.sbml_files = [sbml_file_path]
petab_problem.condition_files = [conditions_tsv_path]
petab_problem.observable_files = [observables_tsv_path]
petab_problem.parameter_files = [parameters_tsv_path]
petab_problem.measurement_files = [measurements_tsv_path]


petab_config = {'format_version': '2.0.0', 'problems': {'my_problem': {
            'sbml_files': petab_problem.sbml_files,
            'measurement_files': petab_problem.measurement_files,
            'parameter_files': petab_problem.parameter_files,
            'condition_files': petab_problem.condition_files,
            'observable_files': petab_problem.observable_files,}}}


output_yaml_path = "/home/PEtab_files/model(EGF).yaml"

# Write the PEtab configuration to a YAML file
with open(output_yaml_path, "w") as yaml_file:
    yaml.dump(petab_config, yaml_file, default_flow_style=False)




# In[ ]:


# NGF Stimulation
parameters = pd.DataFrame({
    'parameterId': ['r0', 'r1', 'r2', 'r3', 'r_1', 'r_2', 'r_3'],
    'parameterScale': ['lin','lin','lin','lin','lin','lin','lin'],
    'lowerBound': [-5, 2.97, 0.2, 0.69, -0.27, -5.85, 0.31],
    'upperBound': [5, 9.11, 0.98, 1.43, -0.07, -1.59, 0.43],
    'nominalValue': [None, None, None, None, None, None, None],
    'estimate': [1, 1, 1, 1, 1, 1, 1]
})




ex_condition = pd.DataFrame({
    'conditionId': ['NGF_stimulation'],
    'conditionName': ['NGF_15_Minutes'],
    'Epo_concentration': ['1.25E-7']  
})



observation = pd.DataFrame({
    'observableId': ['NGF','Raf', 'Mek', 'Erk'],
    'observableName': ['Ngf_stimuli','Raf_kinase','Mek_kinase','Erk_kinase'],
    'observableFormula': ['r0*NGF', 'r0*NGF + r_3*Erk + r1*Raf - r3*Raf',
                          'r1*Raf - r_2*Erk - r_1*Mek - r2*Mek',
                          'r3*Raf - r2*Mek - r_1*Erk - r_3*Erk'],
    'noiseFormula': [None, None, None, None],
    'noiseDistribution': [None, None, None, None]
})




measurement = pd.DataFrame({
    'observableId': ['NGF','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk'],
    'simulationConditionId': ['NGF_stimulation','NGF_stimulation','NGF_stimulation',
                              'NGF_stimulation','NGF_stimulation','NGF_stimulation',
                              'NGF_stimulation','NGF_stimulation','NGF_stimulation',
                              'NGF_stimulation',],
    'measurement': [100,0,0.19,0.9,1,0.67,0.55,0.58,0.5,0.55],
    'time': [0, 0, 100, 280, 420, 600, 840, 1800, 2400, 3000],
    'noiseParameters': [None, None, None, None, None, None, None, None, None, None]
})




visualization =pd.DataFrame({
    'plotId': ['plot_2'],
    'plotTypeData': ['MeanAndSD'],
    'xLabel': ['Time(sec)'],
    'yValues': ['Erk'],
    'yLabel' : ['ppERK']  
})



directory = '/home/PEtab_files/NGF/' 

file_name1 = 'parameters.tsv'
file_name2 = 'ex_condition.tsv'
file_name3 = 'observation.tsv'
file_name4 = 'measurement.tsv'
file_name5 = 'visualization.tsv'


file_path1 = directory + file_name1
file_path2 = directory + file_name2
file_path3 = directory + file_name3
file_path4 = directory + file_name4
file_path5 = directory + file_name5


parameters.to_csv(file_path1, sep='\t', index=False)
ex_condition.to_csv(file_path2, sep='\t', index=False)
observation.to_csv(file_path3, sep='\t', index=False)
measurement.to_csv(file_path4, sep='\t', index=False)
visualization.to_csv(file_path5, sep='\t', index=False)



sbml_file = pd.DataFrame({
    'ID': ['R1', 'R2', 'R3', 'R4', 'R5','R6','R7'],
    'Reaction': ['NGF->Raf','Raf->Mek','Mek->Raf',
                 'Mek->Erk','Erk->Mek','Raf->Erk','Erk->Raf'],
    'Rate law': ['r0 * NGF','r1 * Raf','r_1 * Mek','r2 * Mek',
                 'r_2 * Erk','r3 * Raf','r_3 * Erk']
})


doc = libsbml.SBMLDocument(3, 1)
model = doc.createModel()

for index, row in sbml_file.iterrows():
    
    reaction = model.createReaction()
    reaction.setId(row['ID'])
    reaction.setName(row['Reaction'])
    
    
    kinetic_law = libsbml.KineticLaw(3, 1)  
    kinetic_law.setMath(libsbml.parseL3Formula(row['Rate law']))
    reaction.setKineticLaw(kinetic_law)


sbml_file_path = "/home/PEtab_files/NGF/model(NGF).sbml"
libsbml.writeSBMLToFile(doc, sbml_file_path)




sbml_file_path = "/home/PEtab_files/NGF/model(NGF).sbml"
conditions_tsv_path = "/home/PEtab_files/NGF/ex_condition.tsv"
observables_tsv_path = "/home/PEtab_files/NGF/observation.tsv"
parameters_tsv_path = "/home/PEtab_files/NGF/parameters.tsv"
measurements_tsv_path = "/home/PEtab_files/NGF/measurement.tsv"
visualization_tsv_path = "/home/PEtab_files/NGF/visualization.tsv"


petab_problem = petab.Problem()


petab_problem.sbml_files = [sbml_file_path]
petab_problem.condition_files = [conditions_tsv_path]
petab_problem.observable_files = [observables_tsv_path]
petab_problem.parameter_files = [parameters_tsv_path]
petab_problem.measurement_files = [measurements_tsv_path]


petab_config = {'format_version': '2.0.0', 'problems': {'my_problem': {
            'sbml_files': petab_problem.sbml_files,
            'measurement_files': petab_problem.measurement_files,
            'parameter_files': petab_problem.parameter_files,
            'condition_files': petab_problem.condition_files,
            'observable_files': petab_problem.observable_files,}}}


output_yaml_path = "/home/PEtab_files/NGF/model(NGF).yaml"


with open(output_yaml_path, "w") as yaml_file:
    yaml.dump(petab_config, yaml_file, default_flow_style=False)
   


# In[ ]:


# The bug lies in the code below!!!

yaml_config = os.path.join(output_yaml_path)
petab_problem = pt.Problem.from_yaml(yaml_config)

