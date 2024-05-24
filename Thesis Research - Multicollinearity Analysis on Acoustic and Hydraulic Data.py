#  ============================================================================
#  THESIS RESEARCH - MULTICOLLINEARITY ANALYSIS ON ACOUSTIC AND HYDRAULIC DATA
#  ============================================================================

#  I. IMPORT PYTHON LIBRARIES 
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

#  III. VISUALIZETHE RELATIONSHIP BETWEEN COLUMNS 
sns.pairplot(df)

#  IV. CALCULATE CORRELATION BETWEEN COLUMNS 
corr = df.corr() 
corr_2 = np.round(corr, decimals=2)

#  V. CALCULATE VIF 
def calculate_vif(df, features):    
    vif, tolerance = {}, {}
    # all the features that you want to examine
    for feature in features:
        # extract all the other features you will regress against
        X = [f for f in features if f != feature]        
        X, y = df[X], df[feature]
        # extract r-squared from the fit
        r2 = LinearRegression().fit(X, y).score(X, y)                
        
        # calculate tolerance
        tolerance[feature] = 1 - r2
        # calculate VIF
        vif[feature] = 1/(tolerance[feature])
    # return VIF DataFrame
    return pd.DataFrame({'VIF': vif, 'Tolerance': tolerance})
#VIF_A = calculate_vif(df=df, features=['Mean-TD', 'Peak-TD', 'Peak-FD', 'Kurtosis-FD', 'Press wo Leak',
#        'Press w Leak', 'Delta Press', 'Vel US', 'Vel DS'])
VIF_A = calculate_vif(df=df, features=['Mean-TD', 'Peak-TD', 'Kurtosis-FD', 
        'Press w Leak', 'Delta Press', 'Vel US', 'Vel DS'])

#  VI. PLOT THE HEATMAP 
plt.figure(figsize = (20, 20), dpi= 800) 
#plt.title("Heat Map Analysis on the Integrated Features", fontsize =15)
sns.heatmap(corr_2, cmap="Blues", annot=True, annot_kws={"size": 20})
plt.tick_params(axis = 'x', labelsize = 14) # x font label size
plt.tick_params(axis = 'y', labelsize = 14) # y font label size
#sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
