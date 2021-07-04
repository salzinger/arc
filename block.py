

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

atom=Rubidium()

laserLinewidth = 0.0001 # in GHz
nList = np.arange(65,69)
c6List = []
blockadeRadiusList = []
for n in nList:
    calculation1 = PairStateInteractions(Rubidium(), n, 0, 0.5, n+2, 0, 0.5, 0.5, 0.5)
    state = printStateString(n,0,0.5)+" m_j= 1/2"
    c6 = calculation1.getC6perturbatively(0,0, 5, 35e9)
    blockade = (abs(c6/laserLinewidth))**(1/6.)
    print("C_6 [%s] = %.0f GHz (mu m)^6\t%.1f mu m" % (state,c6,blockade))
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
plt.show()
