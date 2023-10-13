
import numpy as np
import matplotlib.pyplot as plt



"""
Bar-plots for mean global response coefficients (GRC) for EGF and NGF
(5 min) and NGF (15 min) stimulation (mean ± s.d. of n = 4 data sets for each
perturbation). The perturbations are represented on the x axis (Raf siRNA, Mek
siRNA and Erk siRNA). 
"""


grm_egf_5_min_mean = np.mean(grm_egf_5_min, axis=0)
grm_ngf_5_min_mean = np.mean(grm_ngf_5_min, axis=0)
grm_ngf_15_min_mean = np.mean(grm_ngf_15_min, axis=0)

grm_egf_5_min_std = np.std(grm_egf_5_min, axis=0)
grm_ngf_5_min_std = np.std(grm_ngf_5_min, axis=0)
grm_ngf_15_min_std = np.std(grm_ngf_15_min, axis=0)


grm_egf_5_min_var = np.var(grm_egf_5_min, axis=0)
grm_ngf_5_min_var = np.var(grm_ngf_5_min, axis=0)
grm_ngf_15_min_var = np.var(grm_ngf_15_min, axis=0)






x = [i for i in range(11)]
x1 = ['Raf', 'Mek', 'Erk','', 'Raf', 'Mek', 'Erk','', 'Raf', 'Mek', 'Erk']

plt.figure(figsize=(10,7))
plt.bar(x[0:3], grm_egf_5_min_mean[0], yerr=grm_egf_5_min_std[0],capsize=5,
        color=['red','blue','orange'],alpha=0.8)

plt.bar(x[4:7], grm_egf_5_min_mean[1], yerr=grm_egf_5_min_std[1],capsize=5,
        color=['red','blue','orange'] , alpha=0.8)

plt.bar(x[8:], grm_egf_5_min_mean[2], yerr=grm_egf_5_min_std[2],capsize=5,
        color=['red','blue','orange'] , alpha=0.8)

plt.grid(which='both', alpha=0.5, linestyle='--')
plt.ylim(-1.6, 1)
plt.xticks(x, x1)
plt.xlabel('Perturbations from L to R: Raf-siRNA, Mek-siRNA & Erk-siRNA', fontsize=12)
plt.ylabel('Coefficients', fontsize=12)
plt.title('Global Rasponse Coefficients(EGF 5 min)', fontsize=14)

plt.show()







x2 = [i for i in range(11)]
x3 = ['Raf', 'Mek', 'Erk','', 'Raf', 'Mek', 'Erk','', 'Raf', 'Mek', 'Erk']


plt.figure(figsize=(10,7))
plt.bar(x2[0:3], grm_ngf_5_min_mean[0], yerr=grm_ngf_5_min_std[0],capsize=5,
         color=['red','blue','orange'],alpha=0.8)


plt.bar(x2[4:7], grm_ngf_5_min_mean[1], yerr=grm_ngf_5_min_std[1],capsize=5,
        color=['red','blue','orange'] , alpha=0.8)

plt.bar(x2[8:], grm_ngf_5_min_mean[2], yerr=grm_ngf_5_min_std[2],capsize=5,
        color=['red','blue','orange'] , alpha=0.8)


plt.grid(which='both', alpha=0.5, linestyle='--')
plt.ylim(-1, 0.5)
plt.xticks(x2, x3)
plt.xlabel('Perturbations from L to R: Raf-siRNA, Mek-siRNA & Erk-siRNA', fontsize=12)
plt.ylabel('Coefficients', fontsize=12)
plt.title('Global Rasponse Coefficients(NGF 5 min)', fontsize=14)

plt.show()




x4 = [i for i in range(11)]
x5 = ['Raf', 'Mek', 'Erk','', 'Raf', 'Mek', 'Erk','', 'Raf', 'Mek', 'Erk']

plt.figure(figsize=(10,7))
plt.bar(x4[0:3], grm_ngf_15_min_mean[0], yerr=grm_ngf_15_min_std[0],capsize=5,
        color=['red','blue','orange'],alpha=0.8)

plt.bar(x4[4:7], grm_ngf_15_min_mean[1], yerr=grm_ngf_15_min_std[1],capsize=5,
        color=['red','blue','orange'] , alpha=0.8)

plt.bar(x4[8:], grm_ngf_15_min_mean[2], yerr=grm_ngf_15_min_std[2],capsize=5,
        color=['red','blue','orange'] , alpha=0.8)


plt.grid(which='both', alpha=0.5, linestyle='--')
plt.ylim(-1.2, 0.9)
plt.xticks(x4, x5)
plt.xlabel('Perturbations from L to R: Raf-siRNA, Mek-siRNA & Erk-siRNA', fontsize=12)
plt.ylabel('Coefficients', fontsize=12)
plt.title('Global Rasponse Coefficients(NGF 15 min)', fontsize=14)

plt.show()

