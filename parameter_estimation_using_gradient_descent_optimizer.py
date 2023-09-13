#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


class CoefficientFinder:
    
    
    def __init__(self, actual_erk, num_iterations, *params, learning_rate=1e-3, threshold=1e-6):
    
        self.actual_erk = actual_erk
        self.num_iterations = num_iterations
        self.learning_rate = learning_rate 
        self.threshold = threshold
        self.stimuli, self.raf, self.mek, self.erk, self.r1, self.r2, self.r3, self.r_1,self.r_2, self.r_3, self.time = params
        self.d = None
        self.r0 = None
        self.mse = None
        self.populations = None
        
        
        
        
    def mse_calculator(self, simulated_erk):
    
        squared_diff = np.power((self.actual_erk - simulated_erk), 2)
    
        mse = np.mean(squared_diff)
        
        return mse
    
    
    
    def concentration_simulator(self):
        
        
        # initialization
        stimuli_conc = np.zeros(len(self.time))
        raf_conc = np.zeros(len(self.time))
        mek_conc = np.zeros(len(self.time))
        erk_conc = np.zeros(len(self.time))
        
        stimuli_conc[0] = self.stimuli
        raf_conc[0] = self.raf
        mek_conc[0] = self.mek
        erk_conc[0] = self.erk
    
    
        for i in range(1, len(self.time)):
            
            dstimuli_dt  = -self.r0 * stimuli_conc[i-1]
            draf_dt  = self.r0 * stimuli_conc[i-1] + self.r_3 * erk_conc[i-1] + self.r_1 * mek_conc[i-1] - self.r3 * raf_conc[i-1] - self.r1 * raf_conc[i-1]
            dmek_dt  = self.r1 * raf_conc[i-1] + self.r_2 * erk_conc[i-1] - self.r_1 * mek_conc[i-1] - self.r2 * mek_conc[i-1]
            derk_dt  = self.r3 * raf_conc[i-1] + self.r2 * mek_conc[i-1] -self.r_2 * erk_conc[i-1] - self.r_3 * erk_conc[i-1] - self.d * erk_conc[i-1]
        
        
            # Calculate derivatives with respect to d and r0
            der_simulated_wrt_d = -self.d * erk_conc[i-1]
            der_simulated_wrt_r0 = stimuli_conc[i-1] - raf_conc[i-1]
       
            stimuli_conc[i] = stimuli_conc[i-1] + dstimuli_dt
            raf_conc[i] = raf_conc[i-1] + draf_dt
            mek_conc[i] = mek_conc[i-1] + dmek_dt
            erk_conc[i] = erk_conc[i-1] + derk_dt
        
            self.populations = {'Time': time, 'Stimuli': stimuli_conc,
                                'Raf': raf_conc, 'Mek': mek_conc, 'Erk': erk_conc}

        
        return erk_conc, der_simulated_wrt_d, der_simulated_wrt_r0


    
    
    def gradient_descent(self):
        
        # Initialize parameters
        self.d = 0.5
        self.r0 = 1

        mse_prev = np.inf # initialize with a large number 

        for iteration in range(self.num_iterations):
            
            simulated_erk, der_simulated_wrt_d, der_simulated_wrt_r0 = self.concentration_simulator()

            mse = self.mse_calculator(simulated_erk)
            self.mse = mse

            if abs(mse_prev - mse) < self.threshold:  
                break

            # Calculate the gradients (partial derivatives)
            gradient_d = -2 * np.mean((self.actual_erk - simulated_erk) * der_simulated_wrt_d)
            gradient_r0 = -2 * np.mean((self.actual_erk - simulated_erk) * der_simulated_wrt_r0)

            # Update parameters using gradient descent
            self.d -= self.learning_rate * gradient_d
            self.r0 -= self.learning_rate * gradient_r0

            mse_prev = mse  # update the previous mse

        return self.d, self.r0, self.mse, self.populations
    
    
    
time = np.array([0, 100, 280, 420, 600, 840, 1800, 2400, 3000])
erk_conc_ngf = np.array([0, 0.19, 0.9, 1, 0.67, 0.55, 0.58, 0.5, 0.55])

time_in_sec = np.arange(0, 3001, 1)
erk_conc = np.interp(time_in_sec, time, erk_conc_ngf)

num_iter = 10000
params = (50, 0, 0, 0, -0.33, -0.30, -0.47, 0.37, 0.50, 0.15, time_in_sec)

model = CoefficientFinder(erk_conc, num_iter, *params)

d, r0, mse, pops = model.gradient_descent()

print(d)
print(r0)
print(mse)
print(pops)

