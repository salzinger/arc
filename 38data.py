import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy as np               # Import Numerical Python
from IPython.core.display import display, HTML #Import HTML for formatting output

# Define path to ARC root directory (for loading data)
# Define path to ARC root directory (for loading data)
import sys
import os

rootDir = '/Users/Hamamatsu/anaconda3/Lib/site-packages/arc' # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
sys.path.append(rootDir)
#os.chdir('arc')



from arc import *                 #Import ARC (Alkali Rydberg Calculator)


atom=Rubidium87()


n1=5
l1=1
j1=1.5
mj1=1.5
n2=38
l2=0
j2=0.5
mj2=0.5
#Laser Parameters
waist = (2.3*(4*2.1))*10**(-6)
P = 2.9*10**(-3)
q=-1;

rabiFreq = atom.getRabiFrequency(n1, l1, j1, mj1,
                                 n2, l2, j2,
                                 q, P, waist)
print("Control Rabi Frequency = 2 pi x %.2f MHz" %(rabiFreq/(2*pi)*1e-6))

waist = 3*10**(-3)
P = 3.5*10**(-6)

q=1;

rabiFreq = atom.getRabiFrequency(5, 0, 0.5, 0.5,
                                 5, 1, 1.5,
                                 q, P, waist)
print("Probe Rabi Frequency = 2 pi x %.2f MHz" %(rabiFreq/(2*pi)*1e-6)