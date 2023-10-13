
# plot the results of the function local_response_calculator()


grm_egf_5_min_mean = np.mean(grm_egf_5_min, axis=0)
grm_ngf_5_min_mean = np.mean(grm_ngf_5_min, axis=0)
grm_ngf_15_min_mean = np.mean(grm_ngf_15_min, axis=0)


#  Using the mean, calculate the standard deviations for use in the error bars.
grm_egf_5_min_std = np.std(grm_egf_5_min, axis=0)
grm_ngf_5_min_std = np.std(grm_ngf_5_min, axis=0)
grm_ngf_15_min_std = np.std(grm_ngf_15_min, axis=0)


# calculated local response coefficients(the data comes from the article)
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




x = [i for i in range(11)]
x1 = ['M->R',_,'E->R',_, 'R->M',_, 'E->M',_, 'R->E',_, 'M->E']

plt.figure(figsize=(10,7))

plt.bar(x[0], lrm_egf_5min[1][0], color='orange',
        yerr = grm_egf_5_min_std[1][0], capsize = 5, alpha=0.8)

plt.bar(x[2], lrm_egf_5min[-1][0], color = 'orange',
        yerr = grm_egf_5_min_std[-1][0],capsize = 5, alpha = 0.8)

plt.bar(x[4], lrm_egf_5min[0][1], color = 'orange',
        yerr = grm_egf_5_min_std[0][1], capsize = 5, alpha=0.8)

plt.bar(x[6], lrm_egf_5min[-1][1], color = 'orange',
        yerr = grm_egf_5_min_std[-1][1],capsize = 5, alpha=0.8)

plt.bar(x[8], lrm_egf_5min[0][-1], color = 'orange',
        yerr = grm_egf_5_min_std[0][-1],capsize = 5, alpha=0.8)

plt.bar(x[10], lrm_egf_5min[1][-1], color = 'orange',
        yerr = grm_egf_5_min_std[1][-1],capsize = 5, alpha=0.8)

plt.grid(which='both', alpha=0.5, linestyle='--')
plt.ylim(-1.5, 2)
plt.xticks(x, x1)
plt.ylabel('Coefficients', fontsize=12)
plt.title('Local Rasponse Coefficients(EGF 5 min)', fontsize=14)
plt.show()






x2 = [i for i in range(11)]
x3 = ['M->R',_,'E->R',_, 'R->M',_, 'E->M',_, 'R->E',_, 'M->E']

plt.figure(figsize=(10,7))

plt.bar(x2[0], lrm_ngf_5min[1][0], color='red',
        yerr = grm_ngf_5_min_std[1][0],capsize = 5, alpha=0.8)

plt.bar(x2[2], lrm_ngf_5min[-1][0], color = 'red',
        yerr = grm_ngf_5_min_std[-1][0],capsize = 5, alpha=0.8)

plt.bar(x2[4], lrm_ngf_5min[0][1], color = 'red',
        yerr = grm_ngf_5_min_std[0][1],capsize = 5,  alpha=0.8)

plt.bar(x2[6], lrm_ngf_5min[-1][1], color = 'red',
        yerr = grm_ngf_5_min_std[-1][1],capsize = 5,  alpha=0.8)

plt.bar(x2[8], lrm_ngf_5min[0][-1], color = 'red',
        yerr = grm_ngf_5_min_std[0][-1],capsize = 5,  alpha=0.8)


plt.bar(x2[10], lrm_ngf_5min[1][-1], color = 'red',
        yerr = grm_ngf_5_min_std[1][-1],capsize = 5,  alpha=0.8)

plt.grid(which='both', alpha=0.5, linestyle='--')
plt.ylim(-1.5, 2.5)
plt.xticks(x2, x3)
plt.ylabel('Coefficients', fontsize=12)
plt.title('Local Rasponse Coefficients(NGF 5 min)', fontsize=14)
plt.show()






x4 = [i for i in range(11)]
x5 = ['M->R',_,'E->R',_, 'R->M',_, 'E->M',_, 'R->E',_, 'M->E']

plt.figure(figsize=(10,7))

plt.bar(x4[0], lrm_ngf_15min[1][0], color='lightgreen',
        yerr = grm_ngf_15_min_std[1][0],capsize = 5, alpha=1)

plt.bar(x4[2], lrm_ngf_15min[-1][0], color = 'lightgreen',
        yerr = grm_ngf_15_min_std[-1][0],capsize = 5, alpha=1)

plt.bar(x4[4], lrm_ngf_15min[0][1]/10, color = 'darkgreen',
        yerr = grm_ngf_15_min_std[0][1],capsize = 5, alpha=1)

plt.bar(x4[6], lrm_ngf_15min[-1][1]/10, color = 'darkgreen',
        yerr = grm_ngf_15_min_std[-1][1],capsize = 5, alpha=1)

plt.bar(x4[8], lrm_ngf_15min[0][-1], color = 'lightgreen',
        yerr = grm_ngf_15_min_std[0][-1],capsize = 5, alpha=1)

plt.bar(x4[10], lrm_ngf_15min[1][-1], color = 'lightgreen',
        yerr = grm_ngf_15_min_std[1][-1],capsize = 5,alpha=1)

plt.grid(which='both', alpha=0.5, linestyle='--')
plt.ylim(-1, 1.5)
plt.xticks(x4, x5)
plt.ylabel('Coefficients', fontsize=12)
plt.title('Local Rasponse Coefficients(NGF 15 min)', fontsize=14)
plt.show()

