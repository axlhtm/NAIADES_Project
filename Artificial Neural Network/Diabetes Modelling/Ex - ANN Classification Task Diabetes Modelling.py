# =============================================================================
# Ex - ANN Classification Task Diabetes Modelling using SKLearn MLPClassifier
# =============================================================================

#  IMPORT PYTHON LIBRARIES 
import sklearn 
import numpy as np 
import pandas as pd
import tensorflow as tf 
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# LOAD TRAIN AND TEST DATASET
df_train = pd.read_csv("G:/My Drive\Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/Artificial Neural Network/Diabetes Modelling/diabetes_latih.csv")
df_test  = pd.read_csv("G:/My Drive\Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/Artificial Neural Network/Diabetes Modelling/diabetes_uji.csv") 

# DEFINE INDEPENDENT VARIABLE
X_train = np.delete(df_train.values,8,axis=1)
X_test  = np.delete(df_test.values,8,axis=1)

# DEFINE DEPENDENT VARIABLE 
Y_train = df_train.iloc[:,-1].values
Y_test  = df_test.iloc[:,-1].values 

# NORMALIZATION DATA 
X_train = MinMaxScaler().fit_transform(X_train) # Normalisasi data yang memiliki range value yang besar
X_test = MinMaxScaler().fit_transform(X_test) # Normalisasi data yang memiliki range value yang besar

# INITIALISING ANN 
clf = MLPClassifier(hidden_layer_sizes=3, learning_rate_init=0.1, max_iter=100)
clf.fit(X_train, Y_train)

# PREDICTING RESULTS FOR SINGLE POINT
Y_pred = clf.predict(X_test)

# EVALUATING MODEL 
print(round(accuracy_score(Y_test,Y_pred),3))
#ann = tf.keras.models.Sequential() 

# PERFORMING FEATURE SCALING
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test  = sc.transform(X_test)

# INITIALISING ANN
ann = tf.keras.models.Sequential() 

# ADDING HIDDEN AND OUTPUT LAYER 
ann.add(tf.keras.layers.Dense(units=6, activation="relu")) # First hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation="relu")) # Second hidden layer
ann.add(tf.keras.layers.Dense(units=1,activation="sigmoid")) # Output layer

# COMPILING ARTIFICIAL NEURAL NETWORK 
ann.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])

# FITTING ARTIFICIAL NEURAL NETWORK
ann.fit(X_train,Y_train,batch_size=32,epochs = 100)