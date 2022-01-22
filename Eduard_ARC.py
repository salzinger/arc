import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy             # Import Numerical Python
from IPython.core.display import display, HTML #Import HTML for formatting output

# Define path to ARC root directory (for loading data)
# Define path to ARC root directory (for loading data)
import sys
import os



rootDir = '/Users/Hamamatsu/anaconda3/Lib/site-packages/arc' # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
sys.path.append(rootDir)



from arc import *                 #Import ARC (Alkali Rydberg Calculator)

atom = Rubidium()

pqn = []
y = []
ybb = []

for n in xrange(5,40):
    pqn.append(n)

    noBBR = atom.getTransitionRate(30, 0, 0.5, n, 1, 0.5, temperature=0.0)\
            +atom.getTransitionRate(30, 0, 0.5, n, 1, 1.5, temperature=0.0)
    withBBR =  atom.getTransitionRate(30, 0, 0.5, n, 1, 0.5, temperature=300.0)\
            +atom.getTransitionRate(30, 0, 0.5, n, 1, 1.5, temperature=300.0)
    y.append(noBBR)
    ybb.append(withBBR-noBBR)

for l in range(0,10):
    print(atom.getTransitionFrequency(30,l,l-0.5,30,l+1,l-0.5))
    print(atom.getTransitionFrequency(30, l, l-0.5, 30, l+1, l-0.5))


nmin=30  #Minimum n
nmax=30 #Maximum n
lmin=0  #Minimum l
lmax=6  #Maxmium l
fig = plt.figure()
sm = StarkMapResonances(atom,[30,0,0.5,-0.5],atom,[30,1,1.5,0.5])
sm.findResonances()

#Plot Energy Levels of Cesium
levels = LevelPlot(atom)
levels.makeLevels(nmin,nmax,lmin,lmax)
levels.drawLevels()
levels.showPlot()

pqn=np.array(pqn)
y = np.array(y)
ybb = np.array(ybb)

width = 0.4
plt.bar(pqn-width/2.,y,width=width,color="r")
plt.bar(pqn+width/2.,ybb,width=width,color="g")
plt.xlabel("Principal quantum number, $n$")
plt.ylabel(r"Transition rate (s${}^{-1}$)")
plt.title("Transition from 30 $S_{1/2}$ to $n$ $P_{1/2,3/2}$")
plt.legend(("Spontaneous decays","Black-body induced transitions"),fontsize=10)
plt.xlim(4,40)
plt.show()

display(HTML("Lifetime (0 K) &tau;<sub>0</sub> = %.2f &mu;s" % \
             (atom.getStateLifetime(30,0,0.5) *1.e6)))
display(HTML("Lifetime (300 K) &tau;<sub>eff</sub> = %.2f &mu;s" % \
             (atom.getStateLifetime(30,0,0.5,temperature=300.,includeLevelsUpTo=39) *1.e6)))