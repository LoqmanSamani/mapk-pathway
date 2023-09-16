#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Error propagation in MRA estimated by Monte Carlo simulations.
Probability distribution of LRCs for 5 min EGF stimulation,
5 min NGF stimulation and 15 min NGF stimulation.
"""



def monte_carlo_simulator(data, variances, num_simulations, num_perturbations):
    
    coefficient_distributions = {}
    
    # extract coefficients from coefficient-matrix
    raf_mek = data[0,1] 
    raf_erk = data[0,2] 
    mek_raf = data[1,0] 
    mek_erk = data[1,2] 
    erk_mek = data[2,1] 
    erk_raf = data[2,0]
    
    # variances
    raf_mek_var = variances[0,1] 
    raf_erk_var = variances[0,2] 
    mek_raf_var = variances[1,0] 
    mek_erk_var = variances[1,2] 
    erk_mek_var = variances[2,1] 
    erk_raf_var = variances[2,0]
    
    # make lists of coefficients, variances and the name of the coefficients
    coefficients = [raf_mek, raf_erk, mek_raf, mek_erk, erk_raf, erk_mek]
    variances = [raf_mek_var, raf_erk_var, mek_raf_var, mek_erk_var, erk_raf_var, erk_mek_var]
    names = ['raf_mek', 'raf_erk', 'mek_raf', 'mek_erk', 'erk_raf', 'erk_mek']
    
    
    # Perform Monte Carlo simulations
    for i in range(len(coefficients)):
        
        sims = []
        for _ in range(num_simulations):   
           
            sampled_lrcs = np.random.normal(loc = coefficients[i], scale = variances[i])
            sims.append(sampled_lrcs)
        
        coefficient_distributions[names[i]] = sims
        
    return coefficient_distributions


lrm_egf_5min = np.array([
    [-1,  1.11,  0.09],
    [-0.10,  -1, 1.00],
    [-0.53, -0.57, -1]
])

lrm_ngf_5min = np.array([
    [-1,  1.63, 0.16],
    [0.06,  -1, 1.08],
    [0.25, -0.57, -1]
])

lrm_ngf_15min = np.array([
    [-1,  6.18, 0.96],
    [-0.17, -1, 0.63],
    [0.40, -3.73, -1]
])




lrm_egf_5_min_var = np.std(grm_egf_5_min, axis=0)
lrm_ngf_5_min_var = np.std(grm_ngf_5_min, axis=0)
lrm_ngf_15_min_var = np.std(grm_ngf_15_min, axis=0)

grm_egf_5_min_mean = np.mean(grm_egf_5_min, axis=0)
grm_ngf_5_min_mean = np.mean(grm_ngf_5_min, axis=0)
grm_ngf_15_min_mean = np.mean(grm_ngf_15_min, axis=0)


num_simulations = 10000
num_perturbations = 3


m_egf_5_min = monte_carlo_simulator(grm_egf_5_min_mean, lrm_egf_5_min_var, 
                                    num_simulations, num_perturbations)



m_ngf_5_min = monte_carlo_simulator(grm_ngf_5_min_mean, lrm_ngf_5_min_var, 
                                    num_simulations, num_perturbations)
    

m_ngf_15_min = monte_carlo_simulator(grm_ngf_15_min_mean, lrm_ngf_15_min_var, 
                                    num_simulations, num_perturbations)


