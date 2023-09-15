



"""
This code generates PEtab-compatible files for both stimuli(EGF and NGF).
It starts by defining parameter, condition, observation, measurement,
and visualization data as pandas DataFrames for both models.
Then, it converts these DataFrames into TSV files for each model.
Additionally, SBML reaction information is defined using pandas DataFrames
and converted into SBML files. Finally YAML configuration files for PEtab are created. 
"""






import pandas as pd
import libsbml
import petab
import yaml
import os
import benchmark_models_petab as models
import numpy as np
import pypesto
import pypesto.petab







# Using pandas's DataFrame to create tsv tables 


# pandas's dataframes for the first model(EGF as stimuli)
parameter = pd.DataFrame({
    'parameterId': ['EGF','Raf', 'Mek', 'Erk','r0', 'r1', 'r2', 'r3', 'r_1', 'r_2', 'r_3','d','sigma'],
    'parameterScale': ['lin','lin','lin','lin','lin','lin','lin','lin','lin','lin','lin','lin','lin'],
    'lowerBound': [0, 0, 0, 0, 0, 0.78, 0.88, -0.02, -0.37, -0.79, -0.88, 0,0.01],
    'upperBound': [100, 100, 100, 100,  5, 1.52, 1.10, 0.21, 0.12, -0.07, -0.32, 5,0.1],
    'nominalValue': [None, None, None, None,None, None, None, None, None, None, None, None, None],
    'estimate': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
})



ex_condition = pd.DataFrame({
    'conditionId': ['EGF_stimulation'],
    'conditionName': ['EGF_5_Minutes'],
})


observation = pd.DataFrame({
    'observableId': ['EGF','Raf', 'Mek', 'Erk'],
    'observableName': ['Egf_stimuli','Raf_kinase','Mek_kinase','Erk_kinase'],
    'observableFormula': ['r0*EGF', 'r0*EGF + r_3*Erk + r_1*Mek - r3*Raf - r1*Raf',
                          'r1*Raf + r_2*Erk - r_1*Mek - r2*Mek',
                          'r3*Raf + r2*Mek - r_2*Erk - r_3*Erk - d*Erk'],
    'noiseFormula': ['sigma', 'sigma' , 'sigma', 'sigma'],
    'noiseDistribution': ['normal', 'normal', 'normal', 'normal']
})


measurement = pd.DataFrame({
    'observableId': ['EGF','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk'],
    'simulationConditionId': ['EGF_stimulation','EGF_stimulation','EGF_stimulation',
                              'EGF_stimulation','EGF_stimulation','EGF_stimulation',
                              'EGF_stimulation','EGF_stimulation','EGF_stimulation',
                              'EGF_stimulation'],
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



# pandas's dataframes for the second model(NGF as stimuli)

parameter1 = pd.DataFrame({
    'parameterId':['NGF','Raf', 'Mek', 'Erk','r0', 'r1', 'r2', 'r3', 'r_1', 'r_2', 'r_3','d'],
    'parameterScale':['lin','lin','lin','lin','lin','lin','lin','lin','lin','lin','lin','lin'],
    'lowerBound': [0, 0, 0, 0, 0, 2.97, 0.2, 0.69, -0.27, -5.85, 0.31, 0],
    'upperBound': [100, 100, 100, 100, 5, 9.11, 0.98, 1.43, -0.07, -1.59, 0.43, 5],
    'nominalValue': [None, None, None, None, None, None, None, None, None, None, None, None],
    'estimate': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})




ex_condition1 = pd.DataFrame({
    'conditionId': ['NGF_stimulation'],
    'conditionName': ['NGF_15_Minutes'], 
})



observation1 = pd.DataFrame({
    'observableId': ['NGF','Raf', 'Mek', 'Erk'],
    'observableName': ['Ngf_stimuli','Raf_kinase','Mek_kinase','Erk_kinase'],
    'observableFormula': ['r0*NGF', 'r0*EGF + r_3*Erk + r_1*Mek - r3*Raf - r1*Raf',
                          'r1*Raf + r_2*Erk - r_1*Mek - r2*Mek',
                          'r3*Raf + r2*Mek - r_2*Erk - r_3*Erk - d*Erk'],
    'noiseFormula': ['sigma', 'sigma' , 'sigma', 'sigma'],
    'noiseDistribution': ['normal', 'normal', 'normal', 'normal']
})




measurement1 = pd.DataFrame({
    'observableId': ['NGF','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk'],
    'simulationConditionId': ['NGF_stimulation','NGF_stimulation','NGF_stimulation',
                              'NGF_stimulation','NGF_stimulation','NGF_stimulation',
                              'NGF_stimulation','NGF_stimulation','NGF_stimulation',
                              'NGF_stimulation'],
    'measurement': [50, 0, 0.19, 0.9, 1, 0.67, 0.55, 0.58, 0.5, 0.55],
    'time': [0, 0, 100, 280, 420, 600, 840, 1800, 2400, 3000],
    'noiseParameters': [None, None, None, None, None, None, None, None, None, None]
})




visualization1 =pd.DataFrame({
    'plotId': ['plot_2'],
    'plotTypeData': ['MeanAndSD'],
    'xLabel': ['Time(sec)'],
    'yValues': ['Erk'],
    'yLabel' : ['ppERK']  
})






# The directories where the data will be stored

file_path_egf_1 = "/home/loqman/petab_files(1)/egf/parameter.tsv"
file_path_egf_2 = "/home/loqman/petab_files(1)/egf/ex_condition.tsv"
file_path_egf_3 = "/home/loqman/petab_files(1)/egf/observation.tsv"
file_path_egf_4 = "/home/loqman/petab_files(1)/egf/measurement.tsv"
file_path_egf_5 = "/home/loqman/petab_files(1)/egf/visualization.tsv"

file_path_ngf_1 = "/home/loqman/petab_files(1)/ngf/parameter.tsv"
file_path_ngf_2 = "/home/loqman/petab_files(1)/ngf/ex_condition.tsv"
file_path_ngf_3 = "/home/loqman/petab_files(1)/ngf/observation.tsv"
file_path_ngf_4 = "/home/loqman/petab_files(1)/ngf/measurement.tsv"
file_path_ngf_5 = "/home/loqman/petab_files(1)/ngf/visualization.tsv"



# Convert pandas dataframes to tsv files with tab separator

parameter.to_csv(file_path_egf_1,   sep='\t',  index=False)
ex_condition.to_csv(file_path_egf_2,  sep='\t',index=False)
observation.to_csv(file_path_egf_3,  sep='\t', index=False)
measurement.to_csv(file_path_egf_4,  sep='\t', index=False)
visualization.to_csv(file_path_egf_5, sep='\t',index=False)

parameter.to_csv(file_path_ngf_1,    sep='\t',  index=False)
ex_condition.to_csv(file_path_ngf_2, sep='\t',  index=False)
observation.to_csv(file_path_ngf_3,  sep='\t',  index=False)
measurement.to_csv(file_path_ngf_4,  sep='\t',  index=False)
visualization.to_csv(file_path_ngf_5, sep='\t', index=False)




# Using pandas's DataFrame to create sbml files

sbml_file_for_egf = pd.DataFrame({
    'ID': ['R1', 'R2', 'R3', 'R4', 'R5','R6','R7', 'R8'],
    'Reaction': ['EGF -> Raf', 'Raf -> Mek', 'Mek -> Raf', 'Mek -> Erk', 'Erk -> Mek',
                 'Raf -> Erk', 'Erk -> Raf', 'Erk ->'],
    'Rate law': ['r0 * EGF', 'r1 * Raf', 'r_1 * Mek', 'r2 * Mek', 'r_2 * Erk',
                 'r3 * Raf', 'r_3 * Erk', 'd * Erk']
})



sbml_file_for_ngf = pd.DataFrame({
    'ID': ['R1', 'R2', 'R3', 'R4', 'R5','R6','R7', 'R8'],
    'Reaction': ['NGF -> Raf', 'Raf -> Mek', 'Mek -> Raf', 'Mek -> Erk', 'Erk -> Mek',
                 'Raf -> Erk', 'Erk -> Raf', 'Erk ->'],
    'Rate law': ['r0 * EGF', 'r1 * Raf', 'r_1 * Mek', 'r2 * Mek', 'r_2 * Erk',
                 'r3 * Raf', 'r_3 * Erk', 'd * Erk']
})







# create sbml files from pandas's DataFrames

doc = libsbml.SBMLDocument(3, 1)
model = doc.createModel()

for index, row in sbml_file_for_egf.iterrows():
   
    reaction = model.createReaction()
    reaction.setId(row['ID'])
    reaction.setName(row['Reaction'])
    
   
    kinetic_law = libsbml.KineticLaw(3, 1) 
    kinetic_law.setMath(libsbml.parseL3Formula(row['Rate law']))
    reaction.setKineticLaw(kinetic_law)

file_path_egf_6 = "/home/loqman/petab_files(1)/egf/model.sbml"
libsbml.writeSBMLToFile(doc, file_path_egf_6)





doc1 = libsbml.SBMLDocument(3, 1)
model1 = doc1.createModel()

for index, row in sbml_file_for_ngf.iterrows():
   
    reaction1 = model1.createReaction()
    reaction1.setId(row['ID'])
    reaction1.setName(row['Reaction'])
    
   
    kinetic_law1 = libsbml.KineticLaw(3, 1) 
    kinetic_law1.setMath(libsbml.parseL3Formula(row['Rate law']))
    reaction1.setKineticLaw(kinetic_law)

file_path_ngf_6 = "/home/loqman/petab_files(1)/ngf/model.sbml"
libsbml.writeSBMLToFile(doc, file_path_ngf_6)









# Create yaml files from sbml and tsv files



# Defined paths to sbml and tsv files
sbml_egf = "/home/loqman/petab_files(1)/egf/model.sbml"
condition_egf =  "/home/loqman/petab_files(1)/egf/ex_condition.tsv"
observable_egf =  "/home/loqman/petab_files(1)/egf/observation.tsv"
parameter_egf =  "/home/loqman/petab_files(1)/egf/parameter.tsv"
measurement_egf =  "/home/loqman/petab_files(1)/egf/measurement.tsv"
visualization_egf =  "/home/loqman/petab_files(1)/egf/visualization.tsv"


sbml_ngf =  "/home/loqman/petab_files(1)/ngf/model.sbml"
condition_ngf =  "/home/loqman/petab_files(1)/ngf/ex_condition.tsv"
observable_ngf =  "/home/loqman/petab_files(1)/ngf/observation.tsv"
parameter_ngf =  "/home/loqman/petab_files(1)/ngf/parameter.tsv"
measurement_ngf =  "/home/loqman/petab_files(1)/ngf/measurement.tsv"
visualization_ngf =  "/home/loqman/petab_files(1)/ngf/visualization.tsv"




# create petab problems for both datasets
petab_problem_egf = petab.Problem()
petab_problem_egf.sbml_file = [sbml_egf]
petab_problem_egf.condition_file = [condition_egf]
petab_problem_egf.observable_file = [observable_egf]
petab_problem_egf.parameter_file = [parameter_egf]
petab_problem_egf.measurement_file = [measurement_egf]
petab_problem_egf.visualization_file = [visualization_egf]


petab_problem_ngf = petab.Problem()
petab_problem_ngf.sbml_file = [sbml_ngf]
petab_problem_ngf.condition_file = [condition_ngf]
petab_problem_ngf.observable_file = [observable_ngf]
petab_problem_ngf.parameter_file = [parameter_ngf]
petab_problem_ngf.measurement_file = [measurement_ngf]
petab_problem_ngf.visualization_file = [visualization_ngf]




# creates dictionaries to store the PEtab configurations

petab_config_egf = {
    'format_version': '1.0.0',
    'parameter_file': petab_problem_egf.parameter_file,
    'problems': [
        {
            'condition_files': petab_problem_egf.condition_file,
            'measurement_files': petab_problem_egf.measurement_file,
            'sbml_files': petab_problem_egf.sbml_file,
            'observable_files': petab_problem_egf.observable_file,
            'visualization_files': petab_problem_egf.visualization_file
        }
    ]
}




petab_config_ngf = {
    'format_version': '1.0.0',
    'parameter_file': petab_problem_ngf.parameter_file,
    'problems': [
        {
            'condition_files': petab_problem_ngf.condition_file,
            'measurement_files': petab_problem_ngf.measurement_file,
            'sbml_files': petab_problem_ngf.sbml_file,
            'observable_files': petab_problem_ngf.observable_file,
            'visualization_files': petab_problem_ngf.visualization_file
        }
    ]
}




# specify the output yaml files directory
yaml_egf_path = "/home/loqman/petab_files(1)/egf/egf_model.yaml"
yaml_ngf_path = "/home/loqman/petab_files(1)/ngf/ngf_model.yaml"




# write the pEtab configurations to  yaml files
with open(yaml_egf_path, "w") as yaml_file:
    yaml.dump(petab_config_egf, yaml_file, default_flow_style=False)
    
    
with open(yaml_ngf_path, "w") as yaml_file:
    yaml.dump(petab_config_ngf, yaml_file, default_flow_style=False)

