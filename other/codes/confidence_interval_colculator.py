
"""
Calculate the 68% confidence interval:

1)Calculate the Mean:
2)Calculate the Standard Deviation:
3)Calculate the Standard Error: Divide the standard deviation by the 
  square root of the number of data points to get the standard error.
  
4)Calculate the Margin of Error: Multiply the standard error by the 
  appropriate Z-score to get the margin of error.For a 68% confidence
  interval, the Z-score is approximately 1 (since the middle 68% of a
  standard normal distribution falls within 1 standard deviation from the mean).

5)Calculate the Confidence Interval: Subtract and add the margin of error
  to the mean to get the lower and upper bounds of the confidence interval.
  
   Lower Bound = Mean - Margin of Error
   Upper Bound = Mean + Margin of Error
"""

def confidence_of_interval_calculator(data):
    
    # a list of the name of the coefficients
    coeffs = ['raf_mek','raf_erk','mek_raf','mek_erk','erk_raf','erk_mek']
    
   
    values_lst = list(data.values())
    
    values_array = np.array([lst for lst in values_lst])
    
    mean_of_values = np.array([np.mean(lst) for lst in values_array])
  
    std_of_values = np.array([np.std(lst) for lst in values_array])
   
    ste_of_values = std_of_values/np.sqrt(len(values_lst[0]))
    
    lower_bounds = mean_of_values - ste_of_values
    upper_bounds = mean_of_values + ste_of_values
    
    named_lower_bounds = zip(coeffs, lower_bounds)
    named_upper_bounds = zip(coeffs, upper_bounds)
    
    return list(named_lower_bounds), list(named_upper_bounds)
    


    
# Calculated lower and upper bounds for all three datasets    
egf5_lower_bounds, egf5_upper_bounds = confidence_of_interval_calculator(m_egf_5_min)
ngf5_lower_bounds, ngf5_upper_bounds = confidence_of_interval_calculator(m_ngf_5_min)
ngf15_lower_bounds, ngf15_upper_bounds = confidence_of_interval_calculator(m_ngf_15_min)

