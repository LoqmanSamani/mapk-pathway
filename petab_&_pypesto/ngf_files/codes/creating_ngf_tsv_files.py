


"""
This code generates PEtab-compatible file for NGF stimuli.
It starts by defining parameter, condition, observation, measurement,
and visualization data as pandas DataFrames.
Then, it converts these DataFrames into TSV files.
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

experimental_condition = pd.DataFrame({
    'conditionId': ['NGF_stimuli']   
})



measurement = pd.DataFrame({
    'observableId': ['NGF_1','Erk_1','Erk_1','Erk_1','Erk_1','Erk_1','Erk_1','Erk_1','Erk_1',
                     'Erk_1'],
    'simulationConditionId': ['NGF_stimuli','NGF_stimuli','NGF_stimuli','NGF_stimuli',
                              'NGF_stimuli','NGF_stimuli','NGF_stimuli','NGF_stimuli',
                              'NGF_stimuli','NGF_stimuli'],
    'measurement': [50, 0, 0.19, 0.9, 1, 0.67, 0.55, 0.58, 0.5, 0.55],
    'time': [0, 0, 100, 280, 420, 600, 840, 1800, 2400, 3000]
})



observables = pd.DataFrame({
    'observableId': ['NGF_1','Raf_1', 'Mek_1', 'Erk_1'],
    'observableFormula': ['-r0*NGF','(r0*NGF)+(r_3*Erk)+(r_1*Mek)-(r3*Raf)-(r1*Raf)',
                          '(r1*Raf)+(r_2*Erk)-(r_1*Mek)-(r2*Mek)',
                          '(r3*Raf)+(r2*Mek)-(r_2*Erk)-(r_3*Erk)-(d*Erk)'],
    'noiseFormula': ['sigma', 'sigma' , 'sigma', 'sigma'],
    'noiseDistribution': ['normal', 'normal', 'normal', 'normal']
})




parameter = pd.DataFrame({
    'parameterId':    ['r0', 'r1', 'r2', 'r3', 'r_1', 'r_2', 'r_3','d','sigma'],
    'parameterScale':   ['lin','lin','lin','lin','lin','lin','lin','lin','lin'],
     'lowerBound': [-1000,  2.97, 0.2,  0.69, -0.27, -5.85, 0.31, -1000, -1000],
    'upperBound':  [1000,   9.11, 0.98, 1.43, -0.07, -1.59,  0.43, 1000,  1000],
    'nominalValue': [None, 6.18,  0.63, 0.96, -0.17, -3.73, 0.40,  None,  None],
    'estimate':     [1, 0, 0, 0, 0, 0, 0, 1, 1]
})




visualization =pd.DataFrame({
    'plotId': ['plot_1'],
    'plotTypeData': ['MeanAndSD'],
    'xLabel': ['Time(second)'],
    'yValues': ['Erk_1'],
    'yLabel' : ['ppErk']  
})



# The directories where the data will be stored

file_path_egf_1 = "/home/loqman/petab_files(1)/ngf/parameter.tsv"
file_path_egf_2 = "/home/loqman/petab_files(1)/ngf/experimental_condition.tsv"
file_path_egf_3 = "/home/loqman/petab_files(1)/ngf/observables.tsv"
file_path_egf_4 = "/home/loqman/petab_files(1)/ngf/measurement.tsv"
file_path_egf_5 = "/home/loqman/petab_files(1)/ngf/visualization.tsv"



# Convert pandas dataframes to tsv files with tab separator

parameter.to_csv(file_path_egf_1,   sep='\t',  index=False)
experimental_condition.to_csv(file_path_egf_2,  sep='\t',index=False)
observables.to_csv(file_path_egf_3,  sep='\t', index=False)
measurement.to_csv(file_path_egf_4,  sep='\t', index=False)
visualization.to_csv(file_path_egf_5, sep='\t',index=False)

   

