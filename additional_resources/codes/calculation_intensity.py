

"""

The provided Python code conducts a simulation to analyze the relationship
between the size of a matrix and the time it takes to perform certain 
computations on it, specifically the calculation of the local response
matrix based on the global response matrix. This is a valuable experiment 
as it allows us to understand how computational resources are affected by 
matrix size. In the simulation, a series of random matrices with varying 
dimensions are generated, and the local response matrix is calculated by 
applying matrix inversion and multiplication operations on the global response
matrix. The code records the time taken to complete these computations for each 
matrix size and stores the results. The resulting data is then visualized using a 
plot, enabling us to observe how the simulation time varies as the matrix size increases.

"""





import matplotlib.pyplot as plt
import numpy as np
import datetime



def local_response_calculator(shape):
    
    random_matrix = np.random.uniform(-1, 1, size=(shape, shape))
    
    random_matrix_inverse = np.linalg.inv(random_matrix)
    
    diagonal_rm_inv = np.diag(random_matrix_inverse)

    diagonal_Rp_inv_2D = np.diag(diagonal_rm_inv)

    identity_matrix = np.eye(shape)

    diagonal_rp = np.linalg.solve(diagonal_Rp_inv_2D, identity_matrix)

    r_matrix = -np.matmul(np.linalg.inv(diagonal_Rp_inv_2D), random_matrix_inverse)
    
    return r_matrix



def calculation_time(shapes):
    
    times = []
    for shape in shapes:
        start_time = datetime.datetime.now()
        calculation = local_response_calculator(shape)
        end_time = datetime.datetime.now()
        time_delta = end_time - start_time
        milliseconds = time_delta.total_seconds() * 1000
        times.append(milliseconds)
            
    return times


# shape of the matric, which will be used in calculation

shapes = [i for i in range(0, 5005, 5)]




# save the calculation times in a list

simulation_time = calculation_time(shapes)




        
# plot the results 
   
plt.figure(figsize=(10, 7))
plt.style.use('dark_background')

plt.plot(shapes, simulation_time) 


plt.xlabel('Shape of the Matrix', fontsize=12)
plt.ylabel('Simulation Time (millisecond)', fontsize=12)
plt.title('Shape of the Matrix vs. Simulation Time', fontsize=16)


# save the result in a pdf format
plt.savefig('simulation_time.pdf', format='pdf')


plt.show()
        



