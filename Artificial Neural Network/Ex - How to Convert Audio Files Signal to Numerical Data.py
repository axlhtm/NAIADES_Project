# =============================================================================
# EXAMPLE - HOW TO CONVERT AUDIO FILES SIGNAL TO NUMERICAL DATA
# =============================================================================

#  IMPORT PYTHON LIBRARIES
import numpy as np 
import librosa as librosa
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import librosa.display
import pandas as pd 
import os 
from sklearn.model_selection import train_test_split
import splitfolders 
import skimage.io
import scipy.stats as stats
from scipy.fft import fft

#  LOAD AUDIO FILES SIGNAL 
y, sr  = librosa.load("G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data/Noise Signal/59250_nov_rth.wav", sr=32000)
df     = (pd.DataFrame(data=[y])).T # Convert audio signal to dataframe 

#  DISPLAY AUDIO FILES SIGNAL 
librosa.display.waveshow(y, max_points=11025, x_axis='s')

#  SIGNAL DATA FEATURES VARIABLES
## Time Domain
TD_Idx = ['Min', 'Max', 'Mean', 'RMS', 'Var', 'Std', 'Power', 'Peak', 'P2P',
          'CF', 'Skew', 'Kurt', 'FF', 'PI']
Min    = [] # Minimum Value
Max    = [] # Maximum Value
Mean   = [] # Mean Value
Rms    = [] # Root Mean Square Error
Var    = [] # Variance
Std    = [] # Standard Deviation
Power  = [] # Power
Peak   = [] # Peak
P2P    = [] # Peak to Peak
CF     = [] # Crest Factor
Skew   = [] # Skewness
Kurt   = [] # Kurtosis
FF     = [] # Form Facotr
PI     = [] # Pulse Indicator
## Frequency Domain
FD_Idx = ['Max_F', 'Sum_F', 'Mean_F', 'Var_F', 'Peak_F', 'Skew_F', 'Kurt_F']
Max_f  = [] # Maximum of Band Power Spectrum
Sum_f  = [] # Sum of Total Band Power 
Mean_f = [] # Mean of Band Power Spectrum
Var_f  = [] # Variance of Band Power
Peak_f = [] # Peak of Band Power 
Skew_f = [] # Skewness of Band Power 
Kurt_f = [] # Kurtosis of Band Power
FT     = fft(df.values) # Fast Fourier Transform from Time Domain 
S      = np.abs(FT**2)/len(df)

#  SIGNAL FEATURES EXRACTION 
## Time Domain
Min.append(np.min(df.values))
Max.append(np.max(df.values))
Mean.append(np.mean(df.values))
Rms.append(np.sqrt(np.mean(df.values**2)))
Var.append(np.var(df.values))
Std.append(np.std(df.values))
Power.append(np.mean(df.values**2))
Peak.append(np.max(np.abs(df.values)))
P2P.append(np.ptp(df.values))
CF.append(np.max(np.abs(df.values))/np.sqrt(np.mean(df.values**2)))
Skew.append(stats.skew(df.values))
Kurt.append(stats.kurtosis(df.values))
FF.append(np.sqrt(np.mean(df.values**2))/np.mean(df.values))
PI.append(np.max(np.abs(df.values))/np.mean(df.values))
## Frequency Domain 
Max_f.append(np.max(S))
Sum_f.append(np.sum(S))
Mean_f.append(np.mean(S))
Var_f.append(np.var(S))
Peak_f.append(np.max(np.abs(S)))
Skew_f.append(stats.skew(df.values))
Kurt_f.append(stats.kurtosis(df.values))

#  FEATURES ALLOCATION IN DATAFRAME
## Time Domain Features
TD_Features = pd.DataFrame(index = [TD_Idx], 
                           data  = [Min, Max, Mean, Rms, Var, Std, Power,
                                    Peak, P2P, CF, Skew, Kurt, FF, PI])
## Frequency Domain Features
FD_Features = pd.DataFrame(index = [FD_Idx], 
                           data  = [Max_f, Sum_f, Mean_f, Var_f, Peak_f,
                                    Skew_f, Kurt_f])

## Dataset
Features = ['Mean','Peak', 'Peak Frequency','Kurtosis Frequency']
Dataset  = pd.DataFrame(index = [Features], 
                        data  = [Mean, Peak, Peak_f, Kurt_f])