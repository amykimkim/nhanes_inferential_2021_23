import pandas as pd
import scipy.stats as stats


#read in the demographics dataset that is .xpt format
filepath = "DEMO_L.xpt"
df = pd.read_sas(filepath, format='xport')

# Question 1: Is there an association between marital status (married or not married) 
# and education level (bachelor’s degree or higher vs. less than a bachelor’s degree)?


