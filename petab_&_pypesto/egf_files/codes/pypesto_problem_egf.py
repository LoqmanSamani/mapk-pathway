

import amici
import benchmark_models_petab as models
import matplotlib.pyplot as plt
import numpy as np
import petab
import pypesto
import pypesto.optimize as optimize
import pypesto.petab
import pypesto.visualize as visualize
import libsbml
from pypesto.visualize.model_fit import visualize_optimized_model_fit




# Specify the path to the existing YAML file
yaml_egf_path = path


# Load the existing YAML file to create a petab problem
petab_problem_egf = petab.Problem.from_yaml(yaml_egf_path)



# Import the model to pyPESTO and AMICI.
importer = pypesto.petab.PetabImporter(petab_problem_egf)
model = importer.create_model()


# some model properties
print("Model parameters:",list(model.getParameterIds()),"\n")
print("Model const parameters:",list(model.getFixedParameterIds()),"\n")
print("Model outputs: ", list(model.getObservableIds()),"\n")
print("Model states: ",list(model.getStateIds()),"\n")


"""
Output:

Model parameters: ['r0', 'd', 'sigma'] 
Model const parameters: ['r1', 'r_1', 'r2', 'r_2', 'r3', 'r_3'] 
Model outputs:  ['EGF_1', 'Raf_1', 'Mek_1', 'Erk_1'] 
Model states:  ['EGF', 'Raf', 'Mek', 'Erk'] 
"""



# Create an objective function to integrate the model, data, and noise 
converter_config = libsbml.SBMLLocalParameterConverter().getDefaultProperties()
petab_problem_egf.sbml_document.convert(converter_config)

obj = importer.create_objective()

problem = importer.create_problem(obj)


# Optimization step

optimizer = optimize.ScipyOptimizer()
engine = pypesto.engine.MultiProcessEngine()

result = optimize.minimize(problem=problem, optimizer=optimizer, n_starts=10, engine=engine)


# Visualization step

# The optimal function values
print(result.optimize_result.fval)


"""
The Output:

[4109856.3920707037, 6442730.948330322, 25154769.170041848,
 33711820.81391503, 399852417.9550516, inf, inf, inf, inf, inf]
 
 

Strategies Employed:

1) Expanding the Range of r0 and d:
   Initially, we widened the range of values for the parameters r0 and d
   from a small range (0 to 5) to an extensive one (-10000 to 10000).
   Surprisingly, this adjustment didn't yield significant improvements
   in the optimization results.
   

2) Adjusting the Range of Sigma:
   In the quest for improved performance, we considered increasing the
   range of the noise parameter sigma, initially ranging from 0.01 to 0.1,
   to an extensive one (-100 to 100). However, it was observed that this
   change led to exponential increases in optimization time, making it an
   impractical approach. Moreover, setting sigma too high may not align with
   the intended modeling of noise, so caution is advised.
   

3) Expanding Measurement Data:
   To further enhance the model's accuracy, we increased the number of data
   points in the measurement data for Erk concentration. Originally comprising
   just 10 points, we extended it to 3000 points.
   This involved generating approximated Erk concentration values for each
   second of the experiment based on the provided data points. Although this
   approach extended the optimization time, it didn't result in a significant
   improvement in the optimization outcome.
   
   
   # time and concentration based on the data in the article
   time = np.array([0,100,280, 420,600,840,1800,2400,3000])
   erk_conc = np.array([0,0.7,1,0.41,0.1,0.03,0.01,0.01,0.01])
  
   # the approximated erk concentration for each second
   time_in_sec = list(np.arange(0, 3001, 1))
   erk_conc_per_sec = list(np.interp(time_in_sec, time, erk_conc1))

   # use the new time and concentration to generate the measurement.tsv file
   measurement = pd.DataFrame({
         'observableId': ['EGF_1' for _ in range(len(time_in_sec))],
         'simulationConditionId': ['EGF_stimuli' for _ in range(len(time_in_sec))],
         'measurement': erk_conc_per_sec,
         'time': time_in_sec
   })

In summary, while we explored various strategies to improve the optimization results,
none of the tested modifications yielded substantial benefits, and in some cases,
they increased computational demands without commensurate gains in model accuracy.

"""



# The standard pypesto plotting 
ref = visualize.create_references(x=petab_problem_egf.x_nominal_scaled,
                                  fval=obj(petab_problem_egf.x_nominal_scaled))

#visualize.waterfall(result, reference=ref, scale_y="lin")
#visualize.parameters(result, reference=ref)



# visualize the model fit
visualize_optimized_model_fit(petab_problem=petab_problem_egf, result=result, pypesto_problem=problem)


# In[ ]:




