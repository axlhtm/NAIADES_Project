#  ============================================================================
#  THESIS RESEARCH - EXTRACTING FEATURES FROM ACOUSTIC DATA FILES 
#  ============================================================================

#  I. IMPORT PYTHON LIBRARIES
import librosa
import numpy as np
import pandas as pd  
import librosa.display
import scipy.stats as stats

from glob import glob 
from scipy.fft import fft

#  II. LOAD AUDIO FILES SIGNAL 
#cwd    = "G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data"
#src    = glob('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data/More Data/*.wav')
src    = glob('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data/More Data2/*.wav')

#  III. SIGNAL DATA FEATURES VARIABLES 
Audio  = [] # Audio File
Leak   = [] # Leak State
## III.A. Time Domain
TD_Idx = ['Min', 'Max', 'Mean', 'Spread', 'RMS', 'Var', 'Std', 'Power', 'Peak', 
          'P2P', 'CF', 'Skew', 'Kurt', 'FF', 'PI']
Min    = [] # Minimum Value
Max    = [] # Maximum Value
Mean   = [] # Mean Value
Spread = [] # Spread Value
Rms    = [] # Root Mean Square Error
Var    = [] # Variance
Std    = [] # Standard Deviation
Power  = [] # Power
Peak   = [] # Peak
P2P    = [] # Peak to Peak
CF     = [] # Crest Factor
Skew   = [] # Skewness
Kurt   = [] # Kurtosis
FF     = [] # Form Factor
PI     = [] # Pulse Indicator
## III.B. Frequency Domain
FD_Idx = ['Max_F', 'Sum_F', 'Mean_F', 'Var_F', 'Peak_F', 'Skew_F', 'Kurt_F']
Max_f  = [] # Maximum of Band Power Spectrum
Sum_f  = [] # Sum of Total Band Power 
Mean_f = [] # Mean of Band Power Spectrum
Var_f  = [] # Variance of Band Power
Peak_f = [] # Peak of Band Power 
Skew_f = [] # Skewness of Band Power 
Kurt_f = [] # Kurtosis of Band Power

#  IV. SIGNAL FEATURES EXRACTION
for i in range(len(src)): 
    Audio.append(src[i])
    y,sr  = librosa.load(src[i],sr = 32000)
    df = (pd.DataFrame(data=[y])).T # Convert audio signal to dataframe 
    FT = fft(df.values) # Fast Fourier Transform from Time Domain 
    S  = np.abs(FT**2)/len(df)
    ## V.A. Time Domain
    Min.append(np.min(df.values))
    Max.append(np.max(df.values))
    Mean.append(np.mean(df.values))
    Spread.append(np.max(df.values)-np.min(df.values))
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
    if Kurt_f[i] > 7 : 
        Leak.append(1)
    else : 
        Leak.append(0)

#  VI. FEATURES ALLOCATION IN DATAFRAME
data = {'Audo File'     : Audio,
        'Min - TD'      : Min, 
        'Max - TD'      : Max, 
        'Mean - TD'     : Mean,
        'Spread - TD'   : Spread,
        'RMS - TD'      : Rms,
        'Var - TD'      : Var, 
        'Std - TD'      : Std, 
        'Power - TD'    : Power, 
        'Peak - TD'     : Peak,
        'P2P - TD'      : P2P, 
        'CF - TD'       : CF,
        'Skew - TD'     : Skew, 
        'Kurtosis - TD' : Kurt, 
        'FF - TD'       : FF,
        'PI - TD'       : PI,
        'Max_F - FD'    : Max_f,
        'Sum_F - FD'    : Sum_f,
        'Mean_F - FD'   : Mean_f,
        'Var_F - FD'    : Var_f,
        'Peak - FD'     : Peak_f,
        'Skew_F - FD'   : Skew_f,
        'Kurtosis - FD' : Kurt_f,
        'Leak'          : Leak}

feat_dt = {'Mean - TD'     : Mean,
           'Peak - TD'     : Peak,
           'Peak - FD'     : Peak_f, 
           'Kurtosis - FD' : Kurt_f,
           'Leak'          : Leak}

Dataset  = pd.DataFrame(data)
Features = pd.DataFrame(feat_dt)

#  VII. EXPORT DATASET TO CSV 
#Dataset.to_csv (r'G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data/Dataset All Output.csv', index = None, header=True) 
#Features.to_csv (r'G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data/Dataset Features Output.csv', index = None, header=True) 