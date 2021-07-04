

import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy as np               # Import Numerical Python
from IPython.core.display import display, HTML #Import HTML for formatting output

# Define path to ARC root directory (for loading data)
import sys
import os

rootDir = '/Users/Hamamatsu/anaconda3/Lib/site-packages/arc' # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
sys.path.append(rootDir)
#os.chdir('arc')

from arc import *                 #Import ARC (Alkali Rydberg Calculator)

atom=Rubidium()

nmin=65
nmax=70

ns=list()

l=list()

c=list()

d=list()

for x in range(nmin,nmax):
  c.append(30)
  x+1

for x in range(nmin,nmax):
  d.append(24)
  x+1


for n in range(nmin,nmax):
  ns.append(n)
  l.append(atom.getTransitionFrequency(n,0,0.5,n+2,0,0.5))
  print([n,n+2,atom.getTransitionFrequency(n,0,0.5,n+2,0,0.5)/10**9])

for x in range(0,len(l)):
  l[x]=l[x]/10**9







plt.semilogy(ns,l)
#plt.plot(ns,c)
#plt.plot(ns,d)

plt.xlabel('$n$')
plt.ylabel('Level Spacing [GHz]')


plt.show()
