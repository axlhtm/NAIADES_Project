#  ===============================================================================
#  E. ARTIFICIAL NEURAL NETWORKS LEAKAGE MODELLING PREDICTION USING SKLEARN
#  ===============================================================================
#  I. IMPORT PYTHON LIBRARIES\
import os
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier

#  II. LOAD ACOUSTIC SIGNAL DATASET 
os.chdir('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Result/')
os.getcwd()
df  = pd.read_excel(r'Integrated Acoustic and Hydraulic Dataset - All Leak Rate.xlsx', sheet_name='Data Int - All Leak Rate')

#  III. SELECT FEATURES COMBINATION
'''
Select features combination from the integrated features dataset (df). 
User need to select combination for Acoustic Features (AF) and Hydraulic Features (HF)

Acoustic Features (AF) combination consists of
Comb-A : Mean - TD, Peak - TD, and Kurtosis - FD 
Comb-B : Mean - TD, Peak - FD, and Kurtosis - FD
Comb-C : Mean - TD, Peak - TD, Peak - FD, and Kurtosis - FD 

Hydraulic Features (HF) combintation consists of 
Comb-1 : Asumption Leak Rate (LR)
Comb-2 : Delta pressure 
Comb-3 : Assumption Leak Rate (LR) and Delta pressure 

Moreover, since we don't know the rate of leakage that conducted in the network, 
we will assume the value of Leak Rate (LR) starting from 0.125 to 5 with 0.125 increment. 
Merged Features (MF) will indicate if we want to integrate Acoustic Features (AF) with 
Hydraulic  Features (HF) or not. 

Merged Features (MF) combintation consists of 
Yes : Acoustic Features (AF) + Hydraulic Features (HF)
No  : Acoustic Features (AF)
'''
AF = 'Comb-A'
HF = 'Comb-3'
LR = 1.5
MF = 'No'

#  IV. COMBINE FEATURES FROM ACOUSTIC AND HYDRAULIC DATA
def AcousticFeatures(AF) : 
    '''
    This function is built to separate Acoustic Features (AF) from the integrated features dataset (df) 
    based on user  and store it to a new dataframe.
    '''
    global AcousticFeatures 
    if AF == 'Comb-A' :
        AcousticFeatures = pd.DataFrame().assign(Mean_TD=df['Mean - TD'], Peak_TD=df['Peak - TD'], Kurtosis_FD=df['Kurtosis - FD'])
    elif AF == 'Comb-B' : 
        AcousticFeatures = pd.DataFrame().assign(Mean_TD=df['Mean - TD'], Peak_FD=df['Peak - FD'], Kurtosis_FD=df['Kurtosis - FD'])
    else : 
        AcousticFeatures = pd.DataFrame().assign(Mean_TD=df['Mean - TD'], Peak_TD=df['Peak - TD'], Peak_FD=df['Peak - FD'], Kurtosis_FD=df['Kurtosis - FD'])
def HydraulicFeatures(HF, LR) : 
    '''
    This function is built to separate Hydraulic Features (HF) from the integrated features dataset (df) 
    based on user  and store it to a new dataframe.
    '''
    global HydraulicFeatures
    if HF == 'Comb-1' : 
        HydraulicFeatures = pd.DataFrame().assign(Ass_Leak_Rate=df['d ' + str(LR)])
    elif HF == 'Comb-2' : 
        HydraulicFeatures = pd.DataFrame().assign(Delta_Pressure=df['Press wo Leak']-df['d ' + str(LR)])
    else : 
        HydraulicFeatures = pd.DataFrame().assign(Ass_Leak_Rate=df['d ' + str(LR)], Delta_Pressure=df['Press wo Leak']-df['d ' + str(LR)])
def MergedFeatures(MF) : 
    '''
    This function is built to merge the separated features from the Acoustic and Hydraulic part ,
    which will be used as an input the machine learning method.
    '''
    global MergedFeatures 
    if MF == 'Yes' : 
        MergedFeatures = pd.concat([AcousticFeatures, HydraulicFeatures], axis=1, join="inner")
        MergedFeatures["Leak"] = df['Leak']
    else : 
        MergedFeatures = AcousticFeatures
        MergedFeatures["Leak"] = df['Leak']
    
#  V. RUN FEATURES FUNCTION
AcousticFeatures(AF)
HydraulicFeatures(HF, LR)
MergedFeatures(MF)
data = MergedFeatures

#  VI. DATA PREPROCESSING
label = preprocessing.LabelEncoder()
leak = label.fit_transform(data['Leak'])
train, test = train_test_split(data,random_state=42)
X_train = train[train.columns[0:3]]
y_train = train['Leak']
X_test  = test[test.columns[0:3]]
y_test  = test['Leak']

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test  = scaler.transform(X_test)

MLP = MLPClassifier(hidden_layer_sizes=(10,10), max_iter = 100)
MLP.fit(X_train, y_train.values.ravel())

predictions = MLP.predict(X_test)

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test,predictions))