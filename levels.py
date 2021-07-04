# Configure the matplotlib graphics library and configure it to show 

# show figures inline in the notebook
              
import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy as np               # Import Numerical Python
from IPython.core.display import display, HTML #Import HTML for formatting output

# Define path to ARC root directory (for loading data)
import sys, os
rootDir = 'home/qd/Schreibtisch/arc' # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
sys.path.append(rootDir)
os.chdir('arc')

from arc import *                 #Import ARC (Alkali Rydberg Calculator)

atom=Rubidium()

#nmin=48  #Minimum n
#nmax=50 #Maximum n
#lmin=0  #Minimum l
#lmax=1  #Maxmium l

#Plot Energy Levels of Cesium
#levels = LevelPlot(atom)
#levels.makeLevels(nmin,nmax,lmin,lmax)
#levels.drawLevels()
#levels.showPlot()
# plot is interactive when called outside the IPython notebook (e.g. from Python program)



#calculation = StarkMapResonances(Rubidium(),[48,0,0.5,0.5],Rubidium(),[50,0,0.5,0.5])
#calculation.findResonances(47,51,20,np.linspace(0,250,200),energyRange=[-50.e6,10.e6])    
#calculation.showPlot() 


calculation1 = PairStateInteractions(Rubidium(), 69, 0, 0.5, 69, 0, 0.5, 0.5, 0.5,interactionsUpTo = 1)
calculation1.defineBasis( 0., 0., 4, 4,30e9,progressOutput=True)
calculation1.diagonalise(np.linspace(1,15,28),200,progressOutput=True)
    
calculation1.plotLevelDiagram()

for j in range(0,200):
  for l in range(1,15):
    if calculation1.highlight[l][j]>0.3:
      print(calculation1.composition[l][j],"radius:", l,"N of eigenvector:",j,calculation1.highlight[l][j])

print("C3 from level diagram:")
calculation1.getC3fromLevelDiagram(1, 15, showPlot=True, minStateContribution=0.0, resonantBranch=1)
print("C6 from level diagram:")
calculation1.getC6fromLevelDiagram(1, 15, showPlot=True, minStateContribution=0.0)

calculation1.ax.set_xlim(1.0,26.0)
calculation1.ax.set_ylim(-1.0,1.0)
calculation1.showPlot(interactive=True)

print("C6 from perturbation theory:")
c6 = calculation1.getC6perturbatively(0,0, 4, 30e9)
print(c6)

laserLinewidth = 0.001 # in GHz
nList = np.arange(0,5)
c6List = []
blockadeRadiusList = []
for n in nList:
    calculation1 = PairStateInteractions(Rubidium(), 48, 0, 0.5, 48+n, 0, 0.5, 0.5, 0.5)
    state = printStateString(48+n,0,0.5)+" m_j= 1/2"
    c6 = calculation1.getC6perturbatively(0,0, 5, 35e9)
    blockade = (abs(c6/laserLinewidth))**(1/6.)
    print("C_6 [%s] = %.0f GHz (mu m)^6\t%.1f mu m" % (state,c6,blockade))
    c6List.append(c6)
    blockadeRadiusList.append(blockade)




