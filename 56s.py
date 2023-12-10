import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy             # Import Numerical Python
#from IPython.core.display import display, HTML #Import HTML for formatting output

# Define path to ARC root directory (for loading data)
# Define path to ARC root directory (for loading data)
import sys
import os



#rootDir = '/Users/Hamamatsu/anaconda3/Lib/site-packages/arc' # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
#sys.path.append(rootDir)



from arc import *                 #Import ARC (Alkali Rydberg Calculator)

laserLinewidth = 0.004

print("Linewidth [MHz]=", laserLinewidth*1000)
atom=Rubidium87()


print("Energy 56p 3/2", atom.getEnergy(56, 1, 1.5))

print("Energy 56p 1/2", atom.getEnergy(56, 1, 0.5))


print("Energy 55p 3/2", atom.getEnergy(55, 1, 1.5))

print("Energy 55p 1/2", atom.getEnergy(55, 1, 0.5))

print("56p 3/2",atom.getTransitionFrequency(56, 1, 1.5, 56, 0, 0.5)/10**9)
print("56p 1/2",atom.getTransitionFrequency(56, 1, 0.5, 56, 0, 0.5)/10**9)


print("61p 3/2",atom.getTransitionFrequency(61, 1, 1.5, 61, 0, 0.5)/10**9)
print("61p 1/2",atom.getTransitionFrequency(61, 1, 0.5, 61, 0, 0.5)/10**9)
#print("56p -1/2",atom.getTransitionFrequency(56, 1, -0.5, 56, 0, 0.5)/10**6)
#print("56p -3/2",atom.getTransitionFrequency(56, 1, -1.5, 56, 0, 0.5)/10**6)

print("-------------------")

print("55p 3/2",atom.getTransitionFrequency(55, 1, 1.5, 56, 0, 0.5)/10**9)
print("55p 1/2",atom.getTransitionFrequency(55, 1, 0.5, 56, 0, 0.5)/10**9)
#print("55p -1/2",atom.getTransitionFrequency(55, 1, -0.5, 56, 0, 0.5)/10**6)
#print("55p -3/2",atom.getTransitionFrequency(55, 1, -1.5, 56, 0, 0.5)/10**6)


nmin = 5  # Minimum n
nmax = 61  # Maximum n
lmin = 0  # Minimum l
lmax = 1  # Maxmium l

# Plot Energy Levels of Cesium
levels = LevelPlot(atom)
levels.makeLevels(nmin, nmax, lmin, lmax)
levels.drawLevels()
levels.showPlot()