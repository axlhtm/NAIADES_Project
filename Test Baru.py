# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 00:05:44 2023

@author: ihu001
"""

#  ===============================================================
#  C. INTEGRATING ACOUSTIC AND HYDRAULIC FEATURES INTO ONE DATASET
#  ===============================================================
#  I. IMPORT PYTHON LIBRARIES
import os
import pandas as pd

#  II. LOAD ACOUSTIC SIGNAL DATASET 
os.chdir('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Result/')
os.getcwd()
df  = pd.read_excel(r'Integrated Acoustic and Hydraulic Dataset - All Leak Rate on Pressure and Velocity.xlsx', sheet_name='Data Int - All Leak Rate')

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
Int : Acoustic Features (AF) + Hydraulic Features (HF)
AcF : Acoustic Features (AF)
HyF : Hydraulic Features (HF)
'''
AF = 'Comb-A'
HF = 'Comb-3'
LR = 3
MF = 'Int'


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
        HydraulicFeatures = pd.DataFrame().assign(Velocity_US=df['US ' + str(LR)], Velocity_DS=df['DS ' + str(LR)])
    else : 
        #HydraulicFeatures = pd.DataFrame().assign(Ass_Leak_Rate=df['d ' + str(LR)],Delta_Pressure=df['Press wo Leak']-df['d ' + str(LR)], Velocity_US=df['US ' + str(LR)], Velocity_DS=df['DS ' + str(LR)])
        HydraulicFeatures = pd.DataFrame().assign(Ass_Leak_Rate=df['d ' + str(LR)], Velocity_US=df['US ' + str(LR)], Velocity_DS=df['DS ' + str(LR)])
        
def MergedFeatures(MF) : 
    '''
    This function is built to merge the separated features from the Acoustic and Hydraulic part ,
    which will be used as an input the machine learning method.
    '''
    global MergedFeatures 
    if MF == 'Int' : 
        MergedFeatures = pd.concat([AcousticFeatures, HydraulicFeatures], axis=1, join="inner")
        MergedFeatures["Leak"] = df['Leak']
    elif MF == 'AcF' :
        MergedFeatures = AcousticFeatures
        MergedFeatures["Leak"] = df['Leak']
    else : 
        MergedFeatures = HydraulicFeatures
        MergedFeatures["Leak"] = df['Leak']
    
#  V. RUN FEATURES FUNCTION
AcousticFeatures(AF)
HydraulicFeatures(HF, LR)
MergedFeatures(MF)

#  ===============================================================================
#  D. ARTIFICIAL NEURAL NETWORKS LEAKAGE MODELLING PREDICTION WITH INTEGRATED DATA
#  ===============================================================================
#  I. IMPORT PYTHON LIBRARIES
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler 


#  II. BUILD THE DATASET FOR ARTIFICIAL NEURAL NETWORK (ANN) MODEL
def BuildDataset() : 
    global X, Y,trans_MergedFeatures, transf_MergedFeatures
    global X_train, X_valid, X_test, Y_train, Y_valid, Y_test
    #  II.A. DEFINE THE INDEPENDENT VARIABLE AND DEPENDENT VARIABLE
    X = MergedFeatures[MergedFeatures.columns[:-1]].values  # Independent variable which is consisted in Merged Features ()
    Y = MergedFeatures[MergedFeatures.columns[-1]].values   # Dependent variable which is consisted of leak or no leak state
    ## II.B. NORMALIZE THE RANGE VALUE IN THE INDEPENDENT VARIABLE
    scaler   = StandardScaler() 
    X        = scaler.fit_transform(X) 
    data     = np.hstack((X, np.reshape(Y, (-1,1))))
    trans_MergedFeatures = pd.DataFrame(data, columns=MergedFeatures.columns)
    ## II.C. DISPLAY THE NORMALIZED DATASET 
    for i in range(len(MergedFeatures.columns[:-1])) : 
        label = MergedFeatures.columns[i]
        plt.hist(trans_MergedFeatures[trans_MergedFeatures['Leak']==1][label], color='blue', label='Leak State', alpha=0.7, density=True, bins=15)
        plt.hist(trans_MergedFeatures[trans_MergedFeatures['Leak']==0][label], color='red', label='No Leak State', alpha=0.7, density=True, bins=15)
        plt.title(label)
        plt.ylabel("Probability")
        plt.xlabel(label)
        plt.legend()
        plt.show()
    ## II.D. CHECK THE NUMBER OF DATA FOR LEAK AND NO LEAK STATE
    len(trans_MergedFeatures[trans_MergedFeatures['Leak']==0]), len(trans_MergedFeatures[trans_MergedFeatures['Leak']==1])
    over = RandomOverSampler()
    X,Y  = over.fit_resample(X,Y)
    data = np.hstack((X, np.reshape(Y, (-1,1)))) # Merge the data
    transf_MergedFeatures = pd.DataFrame(data, columns=MergedFeatures.columns)
    ## II.E. SPLIT THE DATASET TO TRAINING, VALIDATION AND TESTING DATASET
    X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.4, random_state=0)           # Splitting dataset to training and temporary set
    X_valid, X_test, Y_valid, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=0) # Splitting temporary set to validation and testing set

#  III. RUN THE DATASET FUNCTION 
BuildDataset()

#  IV. RUN THE ARTIFICIAL NEURAL NETWORK (ANN) MODEL
def BuildANN_TF() :
    global model
    ## IV.A. INITIATING ANN MODEL USING TENSOR FLOW
    #model = load_model('G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/ANN Tensor Flow/Comb C/ANN_TF_Comb_C.h5')
    model = tf.keras.Sequential()
    ## III.C. ADD HIDDEN AND OUTPUT LAYERS
    model.add(tf.keras.layers.Dense(units=8, activation="relu"))  # First hidden layer #
    model.add(tf.keras.layers.Dense(units=8, activation="relu"))  # Second hidden layer
    model.add(tf.keras.layers.Dense(units=1, activation="sigmoid")) # Output layer # Sigmoid for binary classification
    ## III.D. COMPILE THE ANN MODEL 
    model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.001), 
                  loss      = tf.keras.losses.BinaryCrossentropy(),
                  metrics   =['accuracy'])
    
    #  IV. RUN THE ARTIFICIAL NEURAL NETWORK (ANN) MODEL
    model.evaluate(X_train, Y_train)
    ## IV.A. FIT THE ANN MODEL TO THE VALIDATION DATASET
    model.fit(X_train,Y_train, batch_size=16, epochs = 100, validation_data=(X_valid, Y_valid)) 
    ## IV.B. FIT THE ANN MODEL TO THE TESTING DATASET 
    model.evaluate(X_test, Y_test)
    
#  V. RUN THE ANN MODEL
BuildANN_TF()


#  V. SAFE THE ANN MODEL
def SaveANN_TF() : 
    model.save('G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/ANN Tensor Flow/Comb C/ANN_TF_Comb_C_1.h5', overwrite=True)
    model.save_weights('G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/ANN Tensor Flow/Comb C/ANN_TF_Comb_C_1_Weight.h5', overwrite=True)
#SaveANN_TF()

def LoadLoadANN_TF() : 
    global new_model
    new_model = load_model('G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/ANN Tensor Flow/Comb C/ANN_TF_Comb_C_1.h5')
    new_model.summary()
    new_model.evaluate(X_test, Y_test)
    
#LoadLoadANN_TF()

def LoadANN_TF() :
    global model
    ## IV.A. INITIATING ANN MODEL USING TENSOR FLOW
    #model = load_model('G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/ANN Tensor Flow/Comb C/ANN_TF_Comb_C.h5')
    model = keras.Sequential()
    ## III.C. ADD HIDDEN AND OUTPUT LAYERS
    model.add(tf.keras.layers.Dense(units=8, activation="relu"))  # First hidden layer #
    model.add(tf.keras.layers.Dense(units=8, activation="relu"))  # Second hidden layer
    model.add(tf.keras.layers.Dense(units=1, activation="sigmoid")) # Output layer # Sigmoid for binary classification
    ## III.D. COMPILE THE ANN MODEL 
    model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.001), 
                  loss      = tf.keras.losses.BinaryCrossentropy(),
                  metrics   =['accuracy'])
    model.load_weigths('G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/ANN Tensor Flow/Comb C/ANN_TF_Comb_C_1_Weight.h5')
    #  IV. RUN THE ARTIFICIAL NEURAL NETWORK (ANN) MODEL
    model.evaluate(X_train, Y_train)
    ## IV.A. FIT THE ANN MODEL TO THE VALIDATION DATASET
    model.fit(X_train,Y_train, batch_size=16, epochs = 100, validation_data=(X_valid, Y_valid)) 
    ## IV.B. FIT THE ANN MODEL TO THE TESTING DATASET 
    model.evaluate(X_test, Y_test)
    
#LoadANN_TF()