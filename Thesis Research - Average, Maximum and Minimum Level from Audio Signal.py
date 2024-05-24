#  ============================================================================
#  THESIS RESEARCH - AVERAGE, MAXIMUM AND MINIMUM LEVEL FROM AUDIO SIGNAL
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
audio_files = glob('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Data CUP Braila/Acoustic Data/More Data/*.wav')

