import numpy as np
"""
The code is for a Monte Carlo simulation, a widely used technique for estimating
the probability distribution of a model's output when the input parameters have 
uncertainty or variability.

Explanation:

1. Input Data and Standard Deviations Information:
   - The function `monte_carlo_simulator` takes as input:
     - `data`: A coefficient matrix  (mean for each set of experimental data)that
               represents the  relationships  between  different model parameters.
     - `std`: A matrix that contains the standard deviations associated with each
              coefficient in the coefficient matrix.
     - `num_simulations`: The number of Monte Carlo simulations to perform.

2. Coefficient Extraction:
   - The code extracts coefficients and standard deviations for various interactions
     between parameters.(`raf_mek`, `raf_erk`, `mek_raf`, `mek_erk`, `erk_raf`, and `erk_mek`) 

3. Coefficient Lists:
   - The code creates lists of coefficients, standard deviations, and the names 
     of the coefficients. The lists are constructed as follows:
     - `coefficients`: A list containing the actual values of the coefficients.
     - `stds`: A list containing the standard deviations associated with each coefficient.
     - `names`: A list containing the names of the coefficients (e.g., 'raf_mek', 'raf_erk', etc.).

4. Monte Carlo Simulations:
   - The heart of this function is the Monte Carlo simulation loop.
   - For each coefficient in the `coefficients` list, the code 
     performs the following steps for `num_simulations`(in this case 10000) iterations:

     a. Sampling from a Normal Distribution:
        - It uses `np.random.normal` to sample from a normal (Gaussian) distribution.
          The normal distribution is characterized by two parameters:
          - `loc`: The mean or expected value of the distribution,
                    which is set to the coefficient value.
          - `scale`: The standard deviation of the distribution.

     b. Collecting Sampled Values:
        - The sampled values (representing the uncertainty in the coefficient) are collected in the `sims` list.

5. Output:
   - The simulation results are stored in the `coefficient_distributions` dictionary,
     where the keys are the names of the coefficients, and the values are lists of sampled 
     values (one list for each coefficient).

"""



def monte_carlo_simulator(data, std, num_simulations):
    
    coefficient_distributions = {}
    
    # extract coefficients from coefficient-matrix
    raf_mek = data[0,1] 
    raf_erk = data[0,2] 
    mek_raf = data[1,0] 
    mek_erk = data[1,2] 
    erk_mek = data[2,1] 
    erk_raf = data[2,0]
    
    # Standard Deviations
    raf_mek_std = std[0,1]
    raf_erk_std = std[0,2]
    mek_raf_std = std[1,0]
    mek_erk_std = std[1,2]
    erk_mek_std = std[2,1]
    erk_raf_std = std[2,0]
    
    # make lists of coefficients, standard deviations and the name of the coefficients
    coefficients = [raf_mek, raf_erk, mek_raf, mek_erk, erk_raf, erk_mek]
    stds = [raf_mek_std, raf_erk_std, mek_raf_std, mek_erk_std, erk_raf_std, erk_mek_std]
    names = ['raf_mek', 'raf_erk', 'mek_raf', 'mek_erk', 'erk_raf', 'erk_mek']
    
    
    # Perform Monte Carlo simulations
    for i in range(len(coefficients)):
        
        sims = []
        for _ in range(num_simulations):   
           
            sampled_lrcs = np.random.normal(loc=coefficients[i], scale=stds[i])
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




lrm_egf_5_min_std = np.std(grm_egf_5_min, axis=0)
lrm_ngf_5_min_std = np.std(grm_ngf_5_min, axis=0)
lrm_ngf_15_min_std = np.std(grm_ngf_15_min, axis=0)

grm_egf_5_min_mean = np.mean(grm_egf_5_min, axis=0)
grm_ngf_5_min_mean = np.mean(grm_ngf_5_min, axis=0)
grm_ngf_15_min_mean = np.mean(grm_ngf_15_min, axis=0)


num_simulations = 10000


m_egf_5_min = monte_carlo_simulator(grm_egf_5_min_mean, lrm_egf_5_min_std, num_simulations)


m_ngf_5_min = monte_carlo_simulator(grm_ngf_5_min_mean, lrm_ngf_5_min_std, num_simulations)
    

m_ngf_15_min = monte_carlo_simulator(grm_ngf_15_min_mean, lrm_ngf_15_min_std, num_simulations)


