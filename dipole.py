import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy as np               # Import Numerical Python
from IPython.core.display import display, HTML #Import HTML for formatting output

# Define path to ARC root directory (for loading data)
import sys, os
rootDir = '/home/qd/anaconda3/lib/python3.5/site-packages/arc' # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
sys.path.append(rootDir)
#os.chdir('arc')



from arc import *                 #Import ARC (Alkali Rydberg Calculator)


atom=Rubidium87()


n1=5
l1=0
j1=0.5
mj1=0.5
n2=5
l2=1
j2=1.5
mj2=1.5


#Radial Matrix element R_{nlj\rightarrown'l'j'}
#print("Dipole matrix element = %.3f ea_0" % atom.getDipoleMatrixElement(n1,l1,j1,mj1,n2,l2,j2,mj2,1))
#Reduced Matrix Element <l||er||l'>
#print("<l||er||l'> = = %.3f ea_0" % atom.getReducedMatrixElementL(n1,l1,j1,n2,l2,j2))
#Reduced Matrix Element <j||er||j'>
#print("<j||er||j'> = %.3f ea_0" % atom.getReducedMatrixElementJ(n1,l1,j1,n2,l2,j2))


nmin=1  #Minimum n
nmax=5 #Maximum n
lmin=1  #Minimum l
lmax=1  #Maxmium l

#Plot Energy Levels of Cesium
#levels = LevelPlot(atom)
#levels.makeLevels(nmin,nmax,lmin,lmax)
#levels.drawLevels()
#levels.showPlot()



print("to 5p to 5p")
print(atom.getTransitionFrequency(5, 1, 1.5, 5, 1, 0.5)/(10**9))
#print("to 49S")
#print(atom.getTransitionFrequency(5, 1, 1.5, 49, 0, 0.5)/(2*10**12))
for n in range(58,59):
	print("to %.0f S - to %.0f P " %(n,n))
	print(atom.getTransitionFrequency(n, 0, 0.5, n, 1, 1.5)/10**9)
	#print((atom.getTransitionFrequency(n, 0, 0.5, n, 1, 0.5)-atom.getTransitionFrequency(n+1, 1, 0.5, n+2, 0, 0.5))/10**9)
	print("to %.0f P - to %.0f S " %(n,n+1))
	print(atom.getTransitionFrequency(n, 1, 0.5, n+1, 0, 0.5)/10**9)

print("to 50p to 500s")
print(3*10**8 * 10**6/atom.getTransitionFrequency(50, 1, 1.5, 500, 0, 0.5))


#print("%.2e Hz" % (1/(2*pi*atom.getStateLifetime(5,1,1.5))) )

#print("69S lifetime in mus:",atom.getStateLifetime(69,0,0.5)*10**6)

#for n in range(64,69):
  #for l in range(0,5):
    #for m in range(-l,l):
   # print((atom.getTransitionFrequency(5, 1, 1.5, n, l, 1/2)-atom.getTransitionFrequency(5, 1, 1.5, 69, 0, 0.5))/(10**9), n,l)

#print((atom.getTransitionFrequency(5, 1, 1.5, 67, 0, 0.5)-atom.getTransitionFrequency(5, 1, 1.5, 67, 2, 2.5))/(2*10**12))
#print(atom.getTransitionFrequency(5, 1, 1.5, 48, 0, 0.5)/(2*10**12))
#print(atom.getTransitionFrequency(5, 1, 1.5, 67, 0, 0.5)/(2*10**12))

#calculation = StarkMapResonances(Rubidium87(),[69,0,0.5,0.5],Rubidium87(),[67,0,0.5,0.5])
#calculation.findResonances(66,70,3,np.linspace(0,100,200),energyRange=[-0.8e9,2.e9])    
#calculation.showPlot()    

#calculation = StarkMapResonances(Rubidium87(),[38,0,0.5,0.5],Rubidium87(),[37,0,0.5,0.5])
#calculation.findResonances(36,40,4,np.linspace(0,500,200),energyRange=[-0.8e9,4.e9])    
#calculation.showPlot()    

n1=5
l1=1
j1=1.5
mj1=1.5
n2=48
l2=0
j2=0.5
mj2=0.5
#Laser Parameters
waist = 60.e-6 
P = 5*10**(-3) 
q=-1; 

#rabiFreq = atom.getRabiFrequency(n1, l1, j1, mj1,
#                                 n2, l2, j2,
#                                 q, P, waist)
#print("Control Rabi Frequency = 2 pi x %.2f MHz" %(rabiFreq/(2*pi)*1e-6))

waist = 3*10**(-3)
P = 20*10**(-6) 

q=1; 

#rabiFreq = atom.getRabiFrequency(5, 0, 0.5, 0.5,
#                                 5, 1, 1.5,
#                                 q, P, waist)
#print("Probe Rabi Frequency = 2 pi x %.2f MHz" %(rabiFreq/(2*pi)*1e-6))

laserLinewidth = 0.0022
dme = atom.getDipoleMatrixElement(48, 0, 0.5, 0.5, 48, 1, 1.5, 1.5, +1)
#dme1 = atom.getDipoleMatrixElement(48, 0, 0.5, 0.5,49, 0, 0.5, 0.5, +1)
#print(dme)
#print(dme1)
c3  = 1/(4.0*pi*epsilon_0)*dme*dme*C_e**2*\
                (physical_constants["Bohr radius"][0])**2 
print("C_3 = %.3f GHz (mu m)^3 " % (abs(c3)/C_h*1.e9  ))
blockade = (abs(abs(c3)/C_h*1.e9/laserLinewidth))**(1/3.)
print("C_3 [48s,48p] = %.0f GHz (mu m)^3\t%.1f mu m" % (abs(c3)/C_h*1.e9,blockade))

laserLinewidth = 0.0022
dme = atom.getDipoleMatrixElement(49, 0, 0.5, 0.5, 48, 1, 1.5, 1.5, 1)
#dme1 = atom.getDipoleMatrixElement(38, 0, 0.5, 0.5, 37, 1, 1.5, 1.5, 1)
#print(dme)
#print(dme1)
c3  = 1/(4.0*pi*epsilon_0)*dme*dme*C_e**2*\
                (physical_constants["Bohr radius"][0])**2 
print("C_3 = %.3f GHz (mu m)^3 " % (abs(c3)/C_h*1.e9  ))
blockade = (abs(abs(c3)/C_h*1.e9/laserLinewidth))**(1/3.)
print("C_3 [49s,48p] = %.0f GHz (mu m)^3\t%.3f mu m" % (abs(c3)/C_h*1.e9,blockade))


calculation1 = PairStateInteractions(Rubidium87(), 67, 0, 0.5, 67, 0, 0.5, 0.5, 0.5)
c6 = calculation1.getC6perturbatively(0,0, 5, 55e9)
blockade = (abs(c6/laserLinewidth))**(1/6.)
print("C_6 [67s] = %.6f GHz (mu m)^6\t%.3f mu m" % (c6,blockade))

calculation1 = PairStateInteractions(Rubidium87(), 48, 0, 0.5, 48, 0, 0.5, 0.5, 0.5)
c6 = calculation1.getC6perturbatively(0,0, 15, 55e9)
blockade = (abs(c6/laserLinewidth))**(1/6.)
print("C_6 [48s] = %.6f GHz (mu m)^6\t%.3f mu m" % (c6,blockade))

calculation1 = PairStateInteractions(Rubidium87(), 49, 0, 0.5, 49, 0, 0.5, 0.5, 0.5)
c6 = calculation1.getC6perturbatively(0,0, 15, 55e9)
blockade = (abs(c6/laserLinewidth))**(1/6.)
print("C_6 [49s] = %.6f GHz (mu m)^6\t%.3f mu m" % (c6,blockade))

calculation1 = PairStateInteractions(Rubidium87(), 48, 0, 0.5, 49, 0, 0.5, 0.5, 0.5)
c6 = calculation1.getC6perturbatively(0,0, 15, 55e9)
blockade = (abs(c6/laserLinewidth))**(1/6.)
print("C_6 [48s,49s] = %.6f GHz (mu m)^6\t%.3f mu m" % (c6,blockade))



print("%.2e Hz : Decay Rate of 5P3/2" % (1/(2*pi*atom.getStateLifetime(5,1,1.5, temperature=50*10**(-6), includeLevelsUpTo=10))) )

print("%.2e Hz : Decay Rate of 5P1/2" % (1/(2*pi*atom.getStateLifetime(5,1,0.5, temperature=50*10**(-6), includeLevelsUpTo=10))) )
print("%.2e Hz : Decay Rate of 39S" % (1/(2*pi*atom.getStateLifetime(39,0,0.5, temperature=50*10**(-6), includeLevelsUpTo=40))) )

print("%.2e us : Lifetime of 38S"% (10**6 *atom.getStateLifetime(38,0,0.5, temperature=300, includeLevelsUpTo=40)) )

print("%.2e us : Lifetime of 39S"% (10**6 *atom.getStateLifetime(39,0,0.5, temperature=50*10**(-6), includeLevelsUpTo=40)) )

