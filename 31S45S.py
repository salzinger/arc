import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy             # Import Numerical Python
from IPython.core.display import display, HTML #Import HTML for formatting output

# Define path to ARC root directory (for loading data)
import sys, os
rootDir = '/home/qd/anaconda3/lib/python3.5/site-packages/arc' # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
sys.path.append(rootDir)
#os.chdir('arc')



from arc import *                 #Import ARC (Alkali Rydberg Calculator)


np=35
ni=36
print("Probe", np)
print("Impurity",ni)
laserLinewidth = 0.006
print("Linewidth [MHz]=", laserLinewidth*1000)
atom=Rubidium87()

calculation = StarkMapResonances(Rubidium87(),[np,0,0.5,0.5],Rubidium87(),[ni,0,0.5,0.5])
calculation.findResonances(np-5,ni+5,4,numpy.linspace(0,3000,200),energyRange=[-2.8e9,1.e9])    
calculation.showPlot() 

pstate1n=30
pstate1j=1.5
pstate1mj=1.5

pstate2n=47
pstate2j=0.5
pstate2mj=0.5      

dme = atom.getDipoleMatrixElement(np, 0, 0.5, 0.5,pstate1n, 1, pstate1j, pstate1mj,1)
dme1 = atom.getDipoleMatrixElement(ni, 0, 0.5, 0.5,pstate2n, 1, pstate2j, pstate2mj,0)
#dme1 = atom.getDipoleMatrixElement(ni, 0, 0.5, 0.5, pstate2n, 1, pstate2j, pstate2mj,1)
print("Dipole Matrix Element [%.0fP,%.0fS]=%.2f" % (pstate1n,np,dme))
print("Dipole Matrix Element [%.0fP,%.0fS]=%.2f" % (pstate2n,ni,dme1))
c3  = 1/(4.0*pi*epsilon_0)*dme*dme1*C_e**2*\
                (physical_constants["Bohr radius"][0])**2 
#print("C_3 = %.3f GHz (mu m)^3 " % (abs(c3)/C_h*1.e9  ))
blockade = (abs(abs(c3)/C_h*1.e9/laserLinewidth))**(1/3.)
print("C_3 [%.0f S,%.0f S] = %.3f GHz (mu m)^3\t%.3f mu m" % (ni,np,abs(c3)/C_h*1.e9,blockade))


calculation1 = PairStateInteractions(Rubidium87(), np, 0, 0.5, np, 0, 0.5, 0.5, 0.5)
c6 = calculation1.getC6perturbatively(0,0, 15, 55e9)

blockade = (abs(c6/laserLinewidth))**(1/6.)

print("C_3/sqrt(C_6)=", abs(c3)/C_h*1.e9/numpy.sqrt(abs(c6)))

print("C_6 [%.0f] = %.6f GHz (mu m)^6\t%.3f mu m" % (np,c6,blockade))


print("%.2f us : Lifetime of %.0f"% (10**6 *atom.getStateLifetime(np,0,0.5, temperature=0, includeLevelsUpTo=40),np))
print("%.2f us : Lifetime of %.0f"% (10**6 *atom.getStateLifetime(ni,0,0.5, temperature=0, includeLevelsUpTo=40),ni))

print("%.2f us : Lifetime of %.0f with BB"% (10**6 *atom.getStateLifetime(np,0,0.5, temperature=300, includeLevelsUpTo=90),np) )
print("%.2f us : Lifetime of %.0f with BB"% (10**6 *atom.getStateLifetime(ni,0,0.5, temperature=300, includeLevelsUpTo=90),ni) )
