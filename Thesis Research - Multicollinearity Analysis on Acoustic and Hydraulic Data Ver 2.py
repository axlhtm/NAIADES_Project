
import os 
import numpy as np
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression 

#  II. LOAD ACOUSTIC SIGNAL DATASET 
os.chdir('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Result/')
os.getcwd()
df  = pd.read_excel(r'Integrated Features.xlsx', sheet_name='Integrated Features')
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 18:24:44 2023

@author: axelh
"""

import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load your dataset
data = df

# Select the independent variables for analysis
#Experiment_0
independent_vars = data[['Mean-TD', 'Peak-TD', 'Peak-FD', 'Kurtosis-FD', 'Press wo Leak', 'Press w Leak', 'Delta Press', 'Vel US', 'Vel DS']]
#Experiment_A1
independent_vars = data[['Mean-TD', 'Peak-TD', 'Kurtosis-FD', 'Press w Leak']]
#Experiment_A2
independent_vars = data[['Mean-TD', 'Peak-TD', 'Kurtosis-FD', 'Delta Press']]
#Experiment_A3
independent_vars = data[['Mean-TD', 'Peak-TD', 'Kurtosis-FD', 'Press w Leak', 'Delta Press']]
#Experiment_A4
independent_vars = data[['Mean-TD', 'Peak-TD', 'Kurtosis-FD', 'Press w Leak', 'Delta Press', 'Vel US', 'Vel DS']]

#Experiment_B1
independent_vars = data[['Mean-TD', 'Peak-FD', 'Kurtosis-FD', 'Press w Leak']]
#Experiment_B2
independent_vars = data[['Mean-TD', 'Peak-FD', 'Kurtosis-FD', 'Delta Press']]
#Experiment_B3
independent_vars = data[['Mean-TD', 'Peak-FD', 'Kurtosis-FD', 'Press w Leak', 'Delta Press']]
#Experiment_A4
independent_vars = data[['Mean-TD', 'Peak-FD', 'Kurtosis-FD', 'Press w Leak', 'Delta Press', 'Vel US', 'Vel DS']]

#Experiment_0
independent_vars = data[['Mean-TD', 'Peak-TD', 'Peak-FD', 'Kurtosis-FD', 'Press wo Leak', 'Press w Leak', 'Delta Press', 'Vel US', 'Vel DS']]
#Experiment_A1

# Calculate the VIF for each independent variable
vif_data = pd.DataFrame()
vif_data['Variable'] = independent_vars.columns
vif_data['VIF'] = [variance_inflation_factor(independent_vars.values, i) for i in range(independent_vars.shape[1])]

# Print the results
print(vif_data)