#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""

The presented code aims to estimate the optimal combination of coefficients,
including the unknowns r0 and degradation, to reproduce experimental data from
the article. However, a significant challenge lies in the high computational cost
associated with the exhaustive search over a vast parameter space. With 10,000
iterations for each unknown coefficient, the total number of simulations becomes
prohibitively large at 100,000,000. This immense computational burden poses practical
limitations and demands consideration of more efficient strategies.

To address this challenge, several potential solutions come to mind.
First, optimization techniques, such as gradient-based methods or genetic
algorithms, can be employed to find an approximate solution with significantly
fewer simulations. These methods aim to iteratively adjust the coefficients to
minimize the difference between simulated and experimental data, effectively 
reducing the need for an exhaustive search. Additionally, it might be possible 
to narrow down the ranges of the unknown coefficients based on prior knowledge 
or additional experimental constraints, further reducing the search space and 
computational load. Striking a balance between accuracy and computational efficiency
is crucial in such parameter estimation tasks, and a combination of these strategies 
could lead to more manageable and practical simulations.

"""


import numpy as np
import matplotlib.pyplot as plt




# the data comes from the article
time = np.array([0,100,280, 420,600,840,1800,2400,3000]) # time in seconds
erk_conc_ngf = np.array([0,0.19,0.9,1,0.67,0.55,0.58,0.5,0.55])
erk_conc_egf = np.array([0,0.7,1,0.41,0.1,0.03,0.01,0.01,0.01])




plt.figure(figsize=(8,5))
plt.plot(time, erk_conc_ngf, label='NGF', color='red', marker='o')
plt.plot(time, erk_conc_egf, label='EGF', color='black', marker='o')
plt.title("Change in ppErk concentration in response to different stimuli.")
plt.ylabel('ppErk')
plt.xlabel('Time')
plt.xlim(0,3500)
plt.ylim(0, 1.1)
plt.grid()
plt.legend()
plt.show()


# In[ ]:


# this function simulates the change in the concentration
# of the individual spesies
def concentration_simulator(stimuli, raf, mek, erk, r0, r1, r2, r3, r_1, r_2, r_3, d, time):
    
    # numpy arrays to save the concentration of each species
    stimuli_conc = np.zeros(len(time))
    raf_conc = np.zeros(len(time))
    mek_conc = np.zeros(len(time))
    erk_conc = np.zeros(len(time))
    
    # initialization
    stimuli_conc[0] = stimuli
    raf_conc[0] = raf
    mek_conc[0] = mek
    erk_conc[0] = erk
    
    
    for i in range(1, len(time)):
        # rates of change
        dstimuli_dt  = -r0 * stimuli_conc[i-1]
        draf_dt  = r0*stimuli_conc[i-1] + r_3*erk_conc[i-1] + r1*raf_conc[i-1] - r3*raf_conc[i-1]
        dmek_dt  = r1*raf_conc[i-1] - r_2*erk_conc[i-1] - r_1*mek_conc[i-1] - r2*mek_conc[i-1]
        derk_dt  = r3*raf_conc[i-1]-r2*mek_conc[i-1]-r_1*erk_conc[i-1]-r_3*erk_conc[i-1] - d
        
        # update the concentrations at the end of each iteration
        stimuli_conc[i] = stimuli_conc[i-1] + dstimuli_dt
        raf_conc[i] = raf_conc[i-1] + draf_dt
        mek_conc[i] = mek_conc[i-1] + dmek_dt
        erk_conc[i] = erk_conc[i-1] + derk_dt
        
    # a dictionary contains the concentration of all species   
    populations = {'Time': time, 'Stimuli': stimuli_conc,
                   'Raf': raf_conc, 'Mek': mek_conc, 'Erk': erk_conc}

        
    return erk_conc, populations


   



# Initial concentrations
egf_0 = 100
ngf_0 = 50
raf_0 = 0
mek_0 = 0
erk_0 = 0



# Using the data from the paper, the concentration in each second is estimated.
time_in_sec = np.arange(0, 3001, 1)
erk_conc_ngf_per_sec = np.interp(time_in_sec, time, erk_conc_ngf)
erk_conc_egf_per_sec = np.interp(time_in_sec, time, erk_conc_egf)


# Ten thousand different coefficients for each unknown coefficient
r0 = np.linspace(1, 5, 10000)
degradation = np.linspace(1, 5, 10000)



# the data are from the article, for each coefficient
# there are 5 measurements, the first four are from the 
# experiments and the last one is the calculated mean from them

# EGF as stimuli
r1 = [-0.86, -0.29, -0.91, 0.13, -0.42]
r2 = [-0.95, -0.19, -0.37, 0.13, -0.35]
r3 = [-1.2, -1.6, -0.28, -0.18, -0.81]
r_1 = [-0.13, 0.27, -0.098, 0.27, 0.08]
r_2 = [1.06, 0.22, 0.11, 0.41, 0.45] 
r_3 = [-0.31, -0.96, -0.23, -0.16, -0.52]

# NGF as stimuli
r11 = [-0.74, 0.10, -0.34, -0.34, -0.33]
r21 = [-0.05, -0.62, -0.26, -0.26, -0.30]
r31 = [-1.15, -0.39, -0.17, -0.17, -0.47]
r_11 = [0.07, 0.09, 0.67, 0.67, 0.37]
r_21 = [0.23, 0.22, 0.59, 0.54, 0.50] 
r_31 = [-0.03, 0.24, 0.34, 0.61, 0.15]






def coefficient_finder(stimuli, raf, mek, erk, r0, r1, r2, r3, r_1, r_2, r_3, d,
                       actual_erk, time, num_iter):
    
    
    infos1 = {}
    for i in range(len(r0)):
        infos = []
        for j in range(num_iter):
            info = []
            for z in range(num_iter):
                erk_conc, _ = concentration_simulator(stimuli, raf, mek, erk, r0[j],r1[i],
                                                         r2[i],r3[i], r_1[i], r_2[i],r_3[i],
                                                         d[z], time)
            
            squared_diff = np.power((actual_erk - erk_conc), 2) 
            mse = np.mean(squared_diff) # Calculate the mean squared error
            info.append((mse,r0[j],d[z], erk))
            
        infos.extend(info)
        
    sorted_infos = sorted(infos, key=lambda x: x[0])
    
    infos1[f'Experiment {i+1}'] = sorted_infos[0]
    
    return infos1
    
egf = coefficient_finder(egf_0, raf_0, mek_0, erk_0, r0, r1, r2, r3, r_1, r_2,
                       r_3, degradation, erk_conc_egf_per_sec, time_in_sec, 10000)

ngf = coefficient_finder(egf_0, raf_0, mek_0, erk_0, r0, r11, r21, r31, r_11, r_21,
                       r_31, degradation, erk_conc_ngf_per_sec, time_in_sec, 10000)

