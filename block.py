

import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy as np               # Import Numerical Python
from IPython.core.display import display, HTML #Import HTML for formatting output

# Define path to ARC root directory (for loading data)
import sys, os
# Define path to ARC root directory (for loading data)
import sys
import os

rootDir = '/Users/Hamamatsu/anaconda3/Lib/site-packages/arc' # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
sys.path.append(rootDir)
#os.chdir('arc')

from arc import *                 #Import ARC (Alkali Rydberg Calculator)

atom=Rubidium87()

laserLinewidth = 0.0004 # in GHz
nList = np.arange(66,69)
c6List = []
blockadeRadiusList = []
for n in nList:
    calculation1 = PairStateInteractions(atom, n, 0, 0.5, n+2, 0, 0.5, 0.5, 0.5)
    state = printStateString(n,0,0.5)+" m_j= 1/2"
    c6 = calculation1.getC6perturbatively(0,0, 5, 35e9)
    blockade = (abs(c6/laserLinewidth))**(1/6.)
    #print("C_6 [%s] = %.0f GHz (mu m)^6\t%.1f mu m" % (state,c6,blockade))
    c6List.append(c6)
    blockadeRadiusList.append(blockade)

ax = plt.subplot(2,1,1)
ax.plot(nList,blockadeRadiusList,"b.")
ax.set_xlabel(r"$n$")
ax.set_ylabel(r"Blockade radius, $r_b$ ($\mu$m)")
ax = plt.subplot(2,1,2)
ax.semilogy(nList,abs(np.array(c6List)),"r.")
ax.set_xlabel(r"$n$")
ax.set_ylabel(r"$C_6$ (GHz $\mu$m$^6$)")
plt.tight_layout()
#plt.show()

calculation1 = PairStateInteractions(atom, 56, 0, 0.5, 56, 0, 0.5, 0.5, 0.5)
state = printStateString(n, 0, 0.5) + " m_j= 1/2"
c6 = calculation1.getC6perturbatively(0, 0, 5, 50e9)
blockade = (abs(c6/laserLinewidth))**(1/6.)
print("C_6 [%s] = %.0f GHz (mu m)^6\t%.1f mu m" % (state,c6,blockade))

dme = atom.getDipoleMatrixElement(56, 0, 0.5, 0.5, 56, 1, 1.5, 1.5, +1)
c3  = 1/(4.0*pi*epsilon_0)*dme*dme*C_e**2*\
                (physical_constants["Bohr radius"][0])**2
blockade = (abs(abs(c3)/C_h*1.e9/laserLinewidth))**(1/3.)
print("blockade %.1f mu m" % (blockade))
print("C_3 = %.3f GHz (mu m)^3 " % (abs(c3)/C_h*1.e9))



dme = atom.getDipoleMatrixElement(56, 0, 0.5, 0.5, 56, 1, 1.5, 1.5, 1)
dme1 = atom.getDipoleMatrixElement(56, 0, 0.5, 0.5, 56, 1, 1.5, 1.5, 1)
c3  = 1/(4.0*pi*epsilon_0)*dme*dme1*C_e**2*\
                (physical_constants["Bohr radius"][0])**2
blockade = (abs(abs(c3)/C_h*1.e9/laserLinewidth))**(1/3.)
print("blockade %.1f mu m" % (blockade))
print("C_3 = %.3f GHz (mu m)^3 " % (abs(c3)/C_h*1.e9))


#calculation = StarkMapResonances(Rubidium87(),[67,0,0.5,0.5],Rubidium87(),[69,0,0.5,0.5])
#calculation.findResonances(61,71,20,np.linspace(10,25,200),energyRange=[-50.e6,10.e6])
#calculation.showPlot()