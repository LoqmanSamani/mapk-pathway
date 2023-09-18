
import pandas as pd
import libsbml
import petab
import yaml
import os
import benchmark_models_petab as models
import numpy as np
import pypesto
import pypesto.petab
from pypesto.visualize.model_fit import visualize_optimized_model_fit


# Specify the paths to your existing YAML files
yaml_egf_path = "/home/loqman/petab_files(1)/egf/egf_model.yaml"




# Load the existing YAML files to create petab problems
petab_problem_egf = petab.Problem.from_yaml(yaml_egf_path)



importer1 = pypesto.petab.PetabImporter(petab_problem_egf)



model1 = importer1.create_model()

print("Model parameters:", list(model1.getParameterIds()), "\n")
print("Model const parameters:", list(model1.getFixedParameterIds()), "\n")
print("Model outputs:   ", list(model1.getObservableIds()), "\n")
print("Model states:    ", list(model1.getStateIds()), "\n")


# To perform parameter estimation, we need to define an objective function.

converter_config = libsbml.SBMLLocalParameterConverter().getDefaultProperties()
petab_problem_egf.sbml_document.convert(converter_config)

obj = importer1.create_objective()


ret = obj(
    petab_problem_egf.x_nominal_scaled,
    mode="mode_fun",
    sensi_orders=(0, 1),
    return_dict=True,
)
print(ret)


# The problem defined in PEtab also defines the fixed parameters and parameter bounds.
# This information is contained in a pypesto.Problem.
problem = importer1.create_problem(obj)
print(problem.x_fixed_indices, problem.x_free_indices)

objective = problem.objective
ret = objective(petab_problem_egf.x_nominal_free_scaled, sensi_orders=(0, 1))
print(ret)
eps = 1e-4


def fd(x):
    grad = np.zeros_like(x)
    j = 0
    for i, xi in enumerate(x):
        mask = np.zeros_like(x)
        mask[i] += eps
        valinc, _ = objective(x + mask, sensi_orders=(0, 1))
        valdec, _ = objective(x - mask, sensi_orders=(0, 1))
        grad[j] = (valinc - valdec) / (2 * eps)
        j += 1
    return grad


fdval = fd(petab_problem_egf.x_nominal_free_scaled)
print("fd: ", fdval)
print("l2 difference: ", np.linalg.norm(ret[1] - fdval))




optimizer = optimize.ScipyOptimizer()

# engine = pypesto.engine.SingleCoreEngine()
engine = pypesto.engine.MultiProcessEngine()

# do the optimization
result = optimize.minimize(
    problem=problem, optimizer=optimizer, n_starts=10, engine=engine
)


result.optimize_result.fval

ref = visualize.create_references(
    x=petab_problem_egf.x_nominal_scaled, fval=obj(petab_problem_egf.x_nominal_scaled)
)

visualize.waterfall(result, reference=ref, scale_y="lin")
visualize.parameters(result, reference=ref)

visualize_optimized_model_fit(petab_problem=petab_problem_egf, result=result, pypesto_problem=problem)
   

