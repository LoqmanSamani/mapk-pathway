

"""
This code generates PEtab-compatible files for EGF stimuli.
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
    'conditionId': ['EGF_stimuli']   
})



measurement = pd.DataFrame({
    'observableId': ['EGF_1','Erk_1','Erk_1','Erk_1','Erk_1','Erk_1','Erk_1','Erk_1','Erk_1',
                     'Erk_1'],
    'simulationConditionId': ['EGF_stimuli','EGF_stimuli','EGF_stimuli','EGF_stimuli',
                              'EGF_stimuli','EGF_stimuli','EGF_stimuli','EGF_stimuli',
                              'EGF_stimuli','EGF_stimuli'],
    'measurement': [100,0.01,0.7,1,0.41,0.1,0.03,0.01,0.01,0.01],
    'time': [0.01, 0.01, 100, 280, 420, 600, 840, 1800, 2400, 3000]
})



observables = pd.DataFrame({
    'observableId': ['EGF_1','Raf_1', 'Mek_1', 'Erk_1'],
    'observableFormula': ['-r0*EGF','(r0*EGF)+(r_3*Erk)+(r_1*Mek)-(r3*Raf)-(r1*Raf)',
                          '(r1*Raf)+(r_2*Erk)-(r_1*Mek)-(r2*Mek)',
                          '(r3*Raf)+(r2*Mek)-(r_2*Erk)-(r_3*Erk)-(d*Erk)'],
    'noiseFormula': ['sigma', 'sigma' , 'sigma', 'sigma'],
    'noiseDistribution': ['normal', 'normal', 'normal', 'normal']
})




parameter = pd.DataFrame({
    'parameterId':    ['r0', 'r1', 'r2', 'r3', 'r_1', 'r_2', 'r_3','d','sigma'],
    'parameterScale':   ['lin','lin','lin','lin','lin','lin','lin','lin','lin'],
    'lowerBound': [-1000, 0.78, 0.88, -0.02, -0.37, -0.79, -0.88, -1000, -1000],
    'upperBound': [1000,  1.52, 1.10,  0.21,  0.12, -0.07, -0.32,  1000,  1000],
    'nominalValue': [None,1.11, 1.08,  0.09,  -0.10,-0.35, -0.53,  None,  None],
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

file_path_egf_1 = ".../parameter.tsv"
file_path_egf_2 = ".../experimental_condition.tsv"
file_path_egf_3 = ".../observables.tsv"
file_path_egf_4 = "...measurement.tsv"
file_path_egf_5 = "...visualization.tsv"


# Convert pandas dataframes to tsv files with tab separator

parameter.to_csv(file_path_egf_1,   sep='\t',  index=False)
experimental_condition.to_csv(file_path_egf_2,  sep='\t',index=False)
observables.to_csv(file_path_egf_3,  sep='\t', index=False)
measurement.to_csv(file_path_egf_4,  sep='\t', index=False)
visualization.to_csv(file_path_egf_5, sep='\t',index=False)

