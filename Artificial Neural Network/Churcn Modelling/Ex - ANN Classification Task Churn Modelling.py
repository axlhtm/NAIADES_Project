#  ============================================================================
#  EXAMPLE - ANN CLASSIFICATION TASK
#  ============================================================================

#  IMPORT PYTHON LIBRARIES
import sklearn 
import numpy as np 
import pandas as pd
import tensorflow as tf 
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# LOAD DATASET
data = pd.read_csv("G:/My Drive\Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/Artificial Neural Network/Churn_Modelling.csv")

# DEFINE INDEPENDENT VARIABLE
X = data.iloc[:,3:-1].values

# DEFINE DEPENDENT VARIABLE 
Y = data.iloc[:,-1].values

# ENCODING CATEGORIAL VARIABLE GENDER
LE1 = LabelEncoder()
X[:,2] = np.array(LE1.fit_transform(X[:,2]))

# ENCODING CATEGORIAL VARIABLE GEOPGRAPHY
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder="passthrough")
X = np.array(ct.fit_transform(X))

# SPLITTING DATASET INTO TRAINING AND TESTING DATASET
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2, random_state=0)

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

# PREDICTING RESULTS FOR SINGLE POINT OBSERVATION
print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1,50000]])) > 0.5)
