#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
This script generates YAML files for configuring parameter estimation
using PEtab and Pypesto.
"""

# Create yaml files from sbml and tsv files


sbml_egf_file = "model.xml"
condition_egf_file = "ex_condition.tsv"
observable_egf_file = "observation.tsv"
parameter_egf_file = "parameter.tsv"
measurement_egf_file = "measurement.tsv"
visualization_egf_file = "visualization.tsv"

sbml_ngf_file = "model.xml"
condition_ngf_file = "ex_condition.tsv"
observable_ngf_file = "observation.tsv"
parameter_ngf_file = "parameter.tsv"
measurement_ngf_file = "measurement.tsv"
visualization_ngf_file = "visualization.tsv"

# Specify the output directory for the YAML files
output_directory = "/home/loqman/petab_files(1)/"

# Create petab problems for both datasets
petab_problem_egf = petab.Problem()
petab_problem_egf.sbml_file = [sbml_egf_file]
petab_problem_egf.condition_file = [condition_egf_file]
petab_problem_egf.observable_file = [observable_egf_file]
petab_problem_egf.parameter_file = [parameter_egf_file]
petab_problem_egf.measurement_file = [measurement_egf_file]
petab_problem_egf.visualization_file = [visualization_egf_file]

petab_problem_ngf = petab.Problem()
petab_problem_ngf.sbml_file = [sbml_ngf_file]
petab_problem_ngf.condition_file = [condition_ngf_file]
petab_problem_ngf.observable_file = [observable_ngf_file]
petab_problem_ngf.parameter_file = [parameter_ngf_file]
petab_problem_ngf.measurement_file = [measurement_ngf_file]
petab_problem_ngf.visualization_file = [visualization_ngf_file]


# Create dictionaries to store the PEtab configurations
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

petab_config_ngf = {
    'format_version': '1.0.0',
    'parameter_file': [parameter_ngf_file],  
    'problems': [
        {
            'condition_files': [condition_ngf_file],  
            'measurement_files': [measurement_ngf_file],  
            'sbml_files': [sbml_ngf_file],  
            'observable_files': [observable_ngf_file],  
            'visualization_files': [visualization_ngf_file],  
        }
    ]
}


# Specify the output YAML file paths
yaml_egf_path = output_directory + "egf_model.yaml"
yaml_ngf_path = output_directory + "ngf_model.yaml"

# Write the PEtab configurations to YAML files
with open(yaml_egf_path, "w") as yaml_file:
    yaml.dump(petab_config_egf, yaml_file, default_flow_style=False)

with open(yaml_ngf_path, "w") as yaml_file:
    yaml.dump(petab_config_ngf, yaml_file, default_flow_style=False)


