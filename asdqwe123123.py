# I. IMPORT PYTHON LIBRARIES
import os 
import librosa
import numpy as np
import pandas as pd  
import librosa.display
import scipy.stats as stats
import matplotlib.pyplot as plt

from glob import glob 
from scipy.fft import fft

# II. LOAD AUDIO FILES SIGNAL 
#cwd    = "G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data"
#y, sr  = librosa.load(cwd+"/More Data/59243_nov_4th.wav", sr=32000)
cwd    = "G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data"
y, sr  = librosa.load(cwd+"/No Leak/rec181944576.wav", sr=32000)
df     = (pd.DataFrame(data=[y])).T # Convert audio signal to dataframe 

# III. DISPLAY AUDIO FILES SIGNAL 
plt.figure(figsize=(7, 7))
plt.plot(np.linspace(0, len(y) / sr, num=len(y)), y)
#plt.xlabel('Time (s)', fontsize=16)  # Increase font size of x-axis
#plt.ylabel('Amplitude', fontsize=16)  # Increase font size of y-axis
#plt.title('Audio Signal in Time Domain', fontsize=16)
plt.show()

# VI. DISPLAY AUDIO FILES SIGNAL IN FREQUENCY DOMAIN (SPECTROGRAM)
#plt.figure(figsize=(14, 5))
plt.figure(figsize=(10, 10))
plt.specgram(y, NFFT=1024, Fs=sr, cmap='jet', noverlap=512)
#plt.xlabel('Time (s)', fontsize=26)  # Increase font size of x-axis
#plt.ylabel('Frequency (Hz)', fontsize=26)  # Increase font size of y-axis
#plt.title('Audio Signal in Spectrogram - Frequency Domain', fontsize=26)
plt.tick_params(axis='both', labelsize=22) 
plt.colorbar(format='%+2.0f dB')
plt.show()

#plt.figure(figsize=(14, 5))
plt.figure(figsize=(10, 10))
plt.plot(np.linspace(0, len(y) / sr, num=len(y)), y)
plt.xlim(0, len(y) / sr)  # Set x-axis range from 0 to the duration of the signal
#plt.xlabel('Time (s)', fontsize=26)  # Increase font size of x-axis
#plt.ylabel('Amplitude', fontsize=26)  # Increase font size of y-axis
#plt.title('Audio Signal in Time Domain', fontsize=26)  # Increase font size of title
plt.tick_params(axis='both', labelsize=22) 
plt.show()

#plt.figure(figsize=(14, 5))
plt.figure(figsize=(10, 10))
plt.specgram(y, NFFT=1024, Fs=sr, cmap='jet', noverlap=512)
#plt.xlabel('Time (s)', fontsize=26)  # Increase font size of x-axis
#plt.ylabel('Frequency (Hz)', fontsize=26)  # Increase font size of y-axis
#plt.title('Audio Signal in Spectrogram - Frequency Domain', fontsize=26)  # Increase font size of title
plt.colorbar(format='%+2.0f dB').remove()  # Remove the colorbar legend
plt.tick_params(axis='both', labelsize=22) 
plt.show()