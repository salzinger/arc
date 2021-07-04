import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy             # Import Numerical Python
from IPython.core.display import display, HTML #Import HTML for formatting output

# Define path to ARC root directory (for loading data)
# Define path to ARC root directory (for loading data)
import sys
import os

rootDir = '/Users/Hamamatsu/anaconda3/Lib/site-packages/arc' # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
sys.path.append(rootDir)
#os.chdir('arc')

from arc import *                 #Import ARC (Alkali Rydberg Calculator)

laserLinewidth = 0.006
print("Linewidth [MHz]=", laserLinewidth*1000)
atom=Rubidium87()

CList=[]
nList=[]

for np in range(18,44):

  ni=np+1
  print("Probe", np)
  print("Impurity",ni)

  calculation1 = PairStateInteractions(Rubidium87(), np, 0, 0.5, np, 0, 0.5, 0.5, 0.5)
  c6 = calculation1.getC6perturbatively(0,0, 15, 55e9)
  c6blockade = (abs(c6/laserLinewidth))**(1/6.)
  
  pstate1n=np
  pstate2n=ni-1

  for pstate1j in [0.5,1.5]:
    for pstate2j in [0.5,1.5]:
      for pstate1mj in [0.5,1.5]:
        for pstate2mj in [0.5,1.5]:
          dme=atom.getDipoleMatrixElement(np,0,0.5,0.5, pstate1n,1,pstate1j,pstate1mj,pstate1mj-0.5)
          dme1=atom.getDipoleMatrixElement(ni,0,0.5,0.5, pstate2n,1,pstate2j,pstate2mj,pstate2mj-0.5)
          print("Dipole Matrix Element [%.0fP,%.0fS]=%.2f" % (pstate1n,np,dme))
          print("Dipole Matrix Element [%.0fP,%.0fS]=%.2f" % (pstate2n,ni,dme1))
          c3  = 1/(4.0*pi*epsilon_0)*dme*dme1*C_e**2*\
                (physical_constants["Bohr radius"][0])**2 
          c3blockade = (abs(c3)/C_h*1.e9/laserLinewidth)**(1/3.)
          print("C_3 [%.0f S,%.0f S] = %.3f GHz (mu m)^3\t%.3f mu m" % (ni,np,abs(c3)/C_h*1.e9,c3blockade) )
          print("C_6 [%.0f] = %.6f GHz (mu m)^6\t%.3f mu m" % (np,c6,c6blockade) )
          cratio=abs(c3)/C_h*1.e9/numpy.sqrt(abs(c6))
          print("C_3/sqrt(C_6)=", cratio )
          CList.append(cratio)
          nList.append([np,pstate1j,pstate2j,pstate1mj,pstate2mj])

  #print("%.2f us : Lifetime of %.0f"% (10**6 *atom.getStateLifetime(np,0,0.5, temperature=0, includeLevelsUpTo=40),np) )
  #print("%.2f us : Lifetime of %.0f"% (10**6 *atom.getStateLifetime(ni,0,0.5, temperature=0, includeLevelsUpTo=40),ni) )

  #print("%.2f us : Lifetime of %.0f with BB"% (10**6 *atom.getStateLifetime(np,0,0.5, temperature=300, includeLevelsUpTo=np+10),np) )
  #print("%.2f us : Lifetime of %.0f with BB"% (10**6 *atom.getStateLifetime(ni,0,0.5, temperature=300, includeLevelsUpTo=ni+10),ni) )
print(nList)
print(CList)
print(numpy.max(CList))
