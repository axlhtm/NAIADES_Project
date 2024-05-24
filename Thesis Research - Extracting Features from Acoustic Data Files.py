#  ============================================================================
#  THESIS RESEARCH - EXTRACTING FEATURES FROM ACOUSTIC DATA FILES 
#  ============================================================================

#  I. IMPORT PYTHON LIBRARIES
import os 
import librosa
import numpy as np
import pandas as pd  
import librosa.display
import scipy.stats as stats

from glob import glob 
from scipy.fft import fft

#  II. LOAD AUDIO FILES SIGNAL 
cwd    = "G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data"
y, sr  = librosa.load(cwd+"/More Data/59243_nov_4th.wav", sr=32000)
df     = (pd.DataFrame(data=[y])).T # Convert audio signal to dataframe 

#  III. DISPLAY AUDIO FILES SIGNAL 
librosa.display.waveshow(y, max_points=11025, x_axis='s')

#  IV. SIGNAL DATA FEATURES VARIABLES
## IV.A. Time Domain
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
## IV.B. Frequency Domain
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

#  V. SIGNAL FEATURES EXRACTION 
## V.A. Time Domain
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
## V.B. Frequency Domain 
Max_f.append(np.max(S))
Sum_f.append(np.sum(S))
Mean_f.append(np.mean(S))
Var_f.append(np.var(S))
Peak_f.append(np.max(np.abs(S)))
Skew_f.append(stats.skew(S))
Kurt_f.append(stats.kurtosis(S))

#  VI. FEATURES ALLOCATION IN DATAFRAME
data = {'Mean - TD'     : Mean,
        'Peak - TD'     : Peak,
        'Peak - FD'     : Peak_f, 
        'Kurtosis - FD' : Kurt_f,
        'Leak'          : 3}
Dataset = pd.DataFrame(data)

#  VII. EXPORT DATASET TO CSV 
#Dataset.to_csv (r'G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data/New Dataset Output.csv', index = None, header=True) 