#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


"""
Calculate local response matrix based on global response matrix with the Modular
response analysis (MRA) method-a sensitivity analysis developed
by Kholodenko et al.
The formula for this calculation is: r = -[diag(Rp⁻1)]⁻1 * Rp⁻1
    Rp : the global response matrix
    r : the network interaction map
       
The function(local_response_calculator)takes the global response matrix(mean)
for each stimuli, calculates the corresponding local response matrix.
"""


def local_response_calculator(grm):
    
    Rp_inv = np.linalg.inv(grm)
    dg_Rp_inv = np.diag(np.diag(Rp_inv))
    dg_Rp_inv_inv = np.linalg.inv(dg_Rp_inv)
    local_response_matrix = -np.matmul(dg_Rp_inv_inv, Rp_inv)
     
    return local_response_matrix





grm_egf_5_min = np.array([
    [[-0.68619036, -0.86058334, -1.20113717],  
    [-0.12842569,  -0.87060372, -0.95215206],
    [-0.31103388,  1.05525896, -0.71368895]],
    [[-1.19055649, -0.29297206, -1.59356725],
    [0.27231917,   0.22774869,   -0.1881955],
    [-0.96319499,  0.22435186, -1.66223414]],
    [[-0.39531907, -0.91250734, -0.28093267],
    [-0.09767814, -0.46534489,  -0.36504135],
    [-0.2286492,   0.11023622, -1.24102056]],
    [[-0.8325981,  0.13465347,  -0.18431002],
    [0.26876685,  -0.04812966,   0.12513944],
    [-0.15890993,  0.41577801, -0.46901709]]

])

grm_ngf_5_min = np.array([
    [[-0.60721868, -0.87840609, -0.99407429],  
    [-0.27618165,  -0.47643055,  -0.8503027],
    [-0.10815451, 0.18410351,  -0.90832514]],
    [[-0.5260274,  0.08170213,   0.06569804],
    [0.06505771,  -0.43478261,   0.06569804],
    [-0.1146789,  0.43036212,  -0.46835953]],
    [[-0.59027266, -0.48844585, -0.38129029],
    [-0.22257351, -0.27600497,  -0.38350765],
    [-0.21738582, 0.19934426,  -0.32152198]],
    [[-0.51637174, -0.09862385,  -0.2380005],
    [-0.09171975,    0.0237581,   -0.149785],
    [-0.14629509,   0.0867747,  -0.8399211]]

])

grm_ngf_15_min = np.array([
    [[-0.50588235, -0.74226422, -1.15392388],  
    [0.07239819,  -0.55260435,   -0.0539592],
    [-0.03098927,  0.23093474, -0.77781074]],
    [[-0.50107066,  0.09848485, -0.39281576],
    [0.08837971,  -0.86039886,  -0.62472196],
    [0.23564955,  0.22363765,  -0.82296651]],
    [[-0.83485873, -0.34045689, -0.16603853],
    [0.66501487,  -0.24947735,  -0.25768709],
    [0.34388366,  0.59179713,  -0.16703809]],
    [[-0.83485873, -0.34045689, -0.16637872],
    [0.66501487,  -0.24947735,  -0.25768709],
    [0.06159032,    0.94167117,  -1.140721]]

])




# mean of global response marricex
grm_egf_5_min_mean = np.mean(grm_egf_5_min, axis=0)
grm_ngf_5_min_mean = np.mean(grm_ngf_5_min, axis=0)
grm_ngf_15_min_mean = np.mean(grm_ngf_15_min, axis=0)

# calculated local response matrices
lrm_egf_5_min = local_response_calculator(grm_egf_5_min_mean)
lrm_ngf_5_min = local_response_calculator(grm_ngf_5_min_mean)
lrm_ngf_15_min = local_response_calculator(grm_ngf_15_min_mean)

