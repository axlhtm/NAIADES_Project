#  ============================================================================
#  THESIS RESEARCH - ARTIFICIAL NEURAL NETWORKS LEAKAGE MODELLING PREDICTION
#  ============================================================================

#  I. IMPORT PYTHON LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler 

#  II. LOAD ACOUSTIC SIGNAL DATASET 
#df = pd.read_excel(r'G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data/CobaANN.xlsx', sheet_name='Sheet1')
#df  = pd.read_excel(r'G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data/Dataset Compilation.xlsx', sheet_name='Dataset Compilation')
df  = pd.read_excel(r'G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data/Dataset Features Output.xlsx', sheet_name='Dataset Features Output')

#df = df.drop(df.columns[-4], axis = 1)
#df = df.drop(df.columns[-2], axis = 1)
#df = df.drop(df.columns[-3], axis = 1)
#df = df.drop(df.columns[-2], axis = 1)
#del df['No.']       # Delete the index coloumn

#  III. DEFINE THE INDEPENDENT VARIABLE AND DEPENDENT VARIABLE
X = df[df.columns[:-1]].values  # Independent variable which is consisted of mean - td, peak - td, and kurtosis - fd
Y = df[df.columns[-1]].values   # Dependent variable which is consisted of leak or no leak state
## III.A. NORMALIZE THE RANGE VALUE IN THE INDEPENDENT VARIABLE
scaler   = StandardScaler() 
X        = scaler.fit_transform(X) 
data     = np.hstack((X, np.reshape(Y, (-1,1))))
trans_df = pd.DataFrame(data, columns=df.columns)
## III.B. DISPLAY THE NORMALIZED DATASET 
for i in range(len(df.columns[:-1])) : 
    label = df.columns[i]
    plt.hist(trans_df[trans_df['Leak']==1][label], color='blue', label='Leak State', alpha=0.7, density=True, bins=15)
    plt.hist(trans_df[trans_df['Leak']==0][label], color='red', label='No Leak State', alpha=0.7, density=True, bins=15)
    plt.title(label)
    plt.ylabel("Probability")
    plt.xlabel(label)
    plt.legend()
    plt.show()
## III.C. CHECK THE NUMBER OF DATA FOR LEAK AND NO LEAK STATE
len(trans_df[trans_df['Leak']==0]), len(trans_df[trans_df['Leak']==1])
over = RandomOverSampler()
X,Y  = over.fit_resample(X,Y)
data = np.hstack((X, np.reshape(Y, (-1,1)))) # Merge the data
transf_df = pd.DataFrame(data, columns=df.columns)

#  IV. BUILD THE ARTIFICIAL NEURAL NETWORK (ANN) MODEL
## IV.A. SPLIT THE DATASET TO TRAINING, VALIDATION AND TESTING DATASET
X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.4, random_state=0)           # Splitting dataset to training and temporary set
X_valid, X_test, Y_valid, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=0) # Splitting temporary set to validation and testing set
## IV.B. INITIATING ANN MODEL 
model = tf.keras.Sequential()
## IV.C. ADD HIDDEN AND OUTPUT LAYERS
model.add(tf.keras.layers.Dense(units=8, activation="relu"))  # First hidden layer #
model.add(tf.keras.layers.Dense(units=8, activation="relu"))  # Second hidden layer
model.add(tf.keras.layers.Dense(units=1,activation="sigmoid")) # Output layer # Sigmoid for binary classification
## IV.D. COMPILE THE ANN MODEL 
model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.001), 
              loss      = tf.keras.losses.BinaryCrossentropy(),
              metrics   =['accuracy'])

#  V. RUN THE ARTIFICIAL NEURAL NETWORK (ANN) MODEL
model.evaluate(X_train, Y_train)
## V.A. FIT THE ANN MODEL TO THE VALIDATION DATASET
model.fit(X_train,Y_train, batch_size=16, epochs = 100, validation_data=(X_valid, Y_valid)) 
## V.B. FIT THE ANN MODEL TO THE TESTING DATASET 
model.evaluate(X_test, Y_test)