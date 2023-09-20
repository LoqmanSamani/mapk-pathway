


sbml_egf_file = "egf_model.xml"
condition_egf_file = "experimental_condition.tsv"
observable_egf_file = "observbles.tsv"
parameter_egf_file = "parameter.tsv"
measurement_egf_file = "measurement.tsv"
visualization_egf_file = "visualization.tsv"


# Specify the output directory for the YAML file
output_directory = "/home/loqman/petab_files(1)/"


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




# Specify the output YAML file path
yaml_egf_path = output_directory + "egf_model.yaml"


# Write the PEtab configuration to YAML file
with open(yaml_egf_path, "w") as yaml_file:
    yaml.dump(petab_config_egf, yaml_file, default_flow_style=False)

    

