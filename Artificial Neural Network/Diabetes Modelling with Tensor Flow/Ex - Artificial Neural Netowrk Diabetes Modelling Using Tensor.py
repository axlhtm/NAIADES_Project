# =============================================================================
#  Ex - Python TensorFlow for Machine Learning Artificial Neural Network
# =============================================================================

# IMPORT PYTHON LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import sklearn 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler 

# LOAD DATASET
df = pd.read_csv("G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/Artificial Neural Network/Diabetes Modelling with Tensor Flow/diabetes.csv")

# DEFINE THE INDEPENDENT AND DEPENDENT VARIABLE
X = df[df.columns[:-1]].values  # INDEPENDENT VARIABLE
Y = df[df.columns[-1]].values   # DEPENDENT VARIABLE 

# NORMALIZE FEATURES SCALE USING STANDARD SCALER
scaler = StandardScaler() 
X = scaler.fit_transform(X) # Our features have different range of values, therefore it needs to be normalized to normal distribution
data = np.hstack((X, np.reshape(Y, (-1,1))))
transform_df = pd.DataFrame(data, columns=df.columns)

# DISPLAY THE DATASET
for i in range(len(df.columns[:-1])) : 
    label = df.columns[i]
    plt.hist(transform_df[transform_df['Outcome']==1][label], color='blue', label='Diabetes', alpha=0.7, density=True, bins=15)
    plt.hist(transform_df[transform_df['Outcome']==0][label], color='red', label='No Diabetes', alpha=0.7, density=True, bins=15)
    # Since the number of data that diagnosed as Diabeters is only 268, while non-diabetes is 500, we would like to normalize the data.
    # Normalize means that we want to compare the histrogram distribution to how many actual values in the data set
    plt.title(label)
    plt.ylabel("Probability")
    plt.xlabel(label)
    plt.legend()
    plt.show()
    

# APPLY RANDOM OVERSAMPLE 
over = RandomOverSampler()
X,Y = over.fit_resample(X,Y)
data = np.hstack((X, np.reshape(Y, (-1,1))))
transform_df = pd.DataFrame(data, columns=df.columns)

# SPLIT THE DATASET TO TRAIN, VALIDATION AND TEST SET 
X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.4, random_state=0)           # SPLITING DEFAULT DATASET TO TRAIN AND TEMPORARY SET
X_valid, X_test, Y_valid, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=0) # SPLITTING TEMP DATASET TO VALIDATION AND TESTING SET

# INITIALISING ANN USING TENSORFLOW 
model = tf.keras.Sequential()

# ADDING HIDDEN AND OUTPUT LAYER 
model.add(tf.keras.layers.Dense(units=16, activation="relu"))  # First hidden layer
model.add(tf.keras.layers.Dense(units=16, activation="relu"))  # Second hidden layer
model.add(tf.keras.layers.Dense(units=1,activation="sigmoid")) # Output layer use sigmoid for binary classification

# COMPILING ARTIFICIAL NEURAL NETWORK 
model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.001), 
              loss      = tf.keras.losses.BinaryCrossentropy(),
              metrics   =['accuracy'])

# EVALUATE ANN MODEL
model.evaluate(X_train, Y_train)

# FITTING ARTIFICIAL NEURAL NETWORK MODEL TO THE VALIDATION DATASET
model.fit(X_train,Y_train, batch_size=16, epochs = 100, validation_data=(X_valid, Y_valid)) 

# FITTING ARTIFICIAL NEURAL NETWORK MODEL TO THE TEST DATASET
model.evaluate(X_test, Y_test)