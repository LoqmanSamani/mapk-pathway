

"""
This code generates PEtab-compatible files for both stimuli(EGF and NGF).
It starts by defining parameter, condition, observation, measurement,
and visualization data as pandas DataFrames for both models.
Then, it converts these DataFrames into TSV files for each model.
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
    'parameterId': ['r0', 'r1', 'r2', 'r3', 'r_1', 'r_2', 'r_3','d','sigma'],
    'parameterScale': ['lin','lin','lin','lin','lin','lin','lin','lin','lin'],
    'lowerBound': [0, 0.78, 0.88, -0.02, -0.37, -0.79, -0.88, 0, 0.01],
    'upperBound': [5, 1.52, 1.10, 0.21, 0.12, -0.07, -0.32, 5, 0.1],
    'nominalValue': [1, 1, 1, 1, 1, 1, 1, 1, 0.01],
    'estimate': [0, 1, 1, 1, 1, 1, 1, 0, 0]
})



ex_condition = pd.DataFrame({
    'conditionId': ['EGF_stimuli'],
    'conditionName': ['EGF_stimulation']
  
})


observation = pd.DataFrame({
    'observableId': ['EGF','Raf', 'Mek', 'Erk'],
    'observableFormula': ['-r0*EGF_stimuli', '(r0*EGF_stimuli)+(r_3*Erk_kinase)+(r_1*Mek_kinase)-(r3*Raf_kinase)-(r1*Raf_kinase)','(r1*Raf_kinase)+(r_2*Erk_kinase)- (r_1*Mek_kinase) - (r2*Mek_kinase)','(r3*Raf_kinase) + (r2*Mek_kinase) - (r_2*Erk_kinase) - (r_3*Erk_kinase)- (d*Erk_kinase)'],
    'noiseFormula': ['sigma', 'sigma' , 'sigma', 'sigma'],
    'noiseDistribution': ['normal', 'normal', 'normal', 'normal']
})



measurement = pd.DataFrame({
    'observableId': ['EGF','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk'],
    'simulationConditionId': ['EGF_stimuli','EGF_stimuli','EGF_stimuli','EGF_stimuli',
                              'EGF_stimuli','EGF_stimuli','EGF_stimuli','EGF_stimuli',
                              'EGF_stimuli','EGF_stimuli'],
    'measurement': [100,0.01,0.7,1,0.41,0.1,0.03,0.01,0.01,0.01],
    'time': [0.01, 0.01, 100, 280, 420, 600, 840, 1800, 2400, 3000]
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
    'parameterId':['r0', 'r1', 'r2', 'r3', 'r_1', 'r_2', 'r_3','d','sigma'],
    'parameterScale':['lin','lin','lin','lin','lin','lin','lin','lin', 'lin'],
    'lowerBound': [0, 2.97, 0.2, 0.69, -0.27, -5.85, 0.31, 0, 0.01],
    'upperBound': [5, 9.11, 0.98, 1.43, -0.07, -1.59, 0.43, 5, 0.1],
    'nominalValue': [1, 1, 1, 1, 1, 1, 1, 1, 0],
    'estimate': [0, 1, 1, 1, 1, 1, 1, 0, 0]
})





ex_condition1 = pd.DataFrame({
    'conditionId': ['NGF_stimuli'],
    'conditionName': ['NGF_stimuli']
    
})



observation1 = pd.DataFrame({
    'observableId': ['NGF','Raf','Mek','Erk'],
    'observableFormula': ['-r0*NGF_stimuli', '(r0*NGF_stimuli) + (r_3*Erk_kinase) +(r_1*Mek_kinase)- (r3*Raf_kinase) - (r1*Raf_kinase)','(r1*Raf_kinase) + (r_2*Erk_kinase) - (r_1*Mek_kinase) - (r2*Mek_kinase)','(r3*Raf_kinase) + (r2*Mek_kinase) - (r_2*Erk_kinase) - (r_3*Erk_kinase)- (d*Erk_kinase)'],
    'noiseFormula': ['sigma', 'sigma' , 'sigma', 'sigma'],
    'noiseDistribution': ['normal', 'normal', 'normal', 'normal']
})





measurement1 = pd.DataFrame({
    'observableId': ['NGF','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk','Erk'],
    'simulationConditionId': ['NGF_stimuli','NGF_stimuli','NGF_stimuli','NGF_stimuli',
                              'NGF_stimuli','NGF_stimuli','NGF_stimuli','NGF_stimuli',
                              'NGF_stimuli','NGF_stimuli'],
    'measurement': [50, 0, 0.19, 0.9, 1, 0.67, 0.55, 0.58, 0.5, 0.55],
    'time': [0, 0, 100, 280, 420, 600, 840, 1800, 2400, 3000]
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


