
# Plot(in form of histograms) the results of the monte carlo simulations

values = list(m_ngf_15_min.values())
plt.figure(figsize=(10,7))
plt.hist(values, bins=1000, alpha=0.7, 
         label=['raf_mek','raf_erk','mek_raf','mek_erk','erk_raf','erk_mek'],
         histtype='stepfilled')

plt.legend()
plt.xlabel('Local Response Coefficient', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('NGF 15 Min', fontsize=14)
plt.show()



values1 = list(m_egf_5_min.values())
plt.figure(figsize=(10,7))
plt.hist(values1, bins=1000, alpha=0.7, 
         label=['raf_mek','raf_erk','mek_raf','mek_erk','erk_raf','erk_mek'],
         histtype='stepfilled')

plt.legend()
plt.xlabel('Local Response Coefficient', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('EGF 5 Min', fontsize=14)
plt.show()





values2 = list(m_ngf_5_min.values())
plt.figure(figsize=(10,7))
plt.hist(values2, bins=1000, alpha=0.7, 
         label=['raf_mek','raf_erk','mek_raf','mek_erk','erk_raf','erk_mek'],
         histtype='stepfilled')

plt.legend()
plt.xlabel('Local Response Coefficient', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('NGF 5 Min', fontsize=14)
plt.show()

