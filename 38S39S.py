import matplotlib.pyplot as plt  # Import library for direct plotting functions
import numpy  # Import Numerical Python
from IPython.core.display import display, HTML  # Import HTML for formatting output

# Define path to ARC root directory (for loading data)
import sys, os

rootDir = '/home/qd/anaconda3/lib/python3.5/site-packages/arc'  # e.g. '/Users/Username/Desktop/ARC-Alkali-Rydberg-Calculator'
sys.path.append(rootDir)
# os.chdir('arc')


from arc import *  # Import ARC (Alkali Rydberg Calculator)

np = 38
ni = 39
print("Probe", np)
print("Impurity", ni)
laserLinewidth = 0.001
print("Linewidth [MHz]=", laserLinewidth * 1000)
atom = Rubidium87()

# calculation = StarkMapResonances(Rubidium87(),[np,0,0.5,0.5],Rubidium87(),[ni,0,0.5,0.5])
# calculation.findResonances(np-5,ni+5,4,numpy.linspace(0,500,200),energyRange=[-0.8e9,1.e9])
# calculation.showPlot()

pstate1n = 38
pstate1j = 1.5
pstate1mj = 1.5

pstate2n = 38
pstate2j = 1.5
pstate2mj = 1.5

dme = atom.getDipoleMatrixElement(pstate1n, 1, pstate1j, pstate1mj, np, 0, 0.5, 0.5, -1)
dme1 = atom.getDipoleMatrixElement(ni, 0, 0.5, 0.5, pstate2n, 1, pstate2j, pstate2mj, 1)
# dme1 = atom.getDipoleMatrixElement(ni, 0, 0.5, 0.5, 34, 1, 1.5, 1.5,1)
print("Dipole Matrix Element [%.0fP,%.0fS]=%.2f" % (pstate1n, np, dme))
print("Dipole Matrix Element [%.0fP,%.0fS]=%.2f" % (pstate2n, ni, dme1))
c3 = 1 / (4.0 * pi * epsilon_0) * dme * dme1 * C_e ** 2 * \
     (physical_constants["Bohr radius"][0]) ** 2
print("C_3 = %.3f GHz (mu m)^3 " % (abs(c3)/C_h*1.e9  ))
blockade = (abs(abs(c3) / C_h * 1.e9 / laserLinewidth)) ** (1 / 3.)
print("C_3 [%.0f S,%.0f S] = %.3f GHz (mu m)^3\t%.3f mu m" % (ni, np, abs(c3) / C_h * 1.e9, blockade))

calculation1 = PairStateInteractions(Rubidium87(), np, 0, 0.5, np, 0, 0.5, 0.5, 0.5)
c6 = calculation1.getC6perturbatively(0, 0, 15, 55e9)

blockade = (abs(c6 / laserLinewidth)) ** (1 / 6.)

print("C_3/sqrt(C_6)=", abs(c3) / C_h * 1.e9 / numpy.sqrt(abs(c6)))

print("C_6 [%.0f] = %.6f GHz (mu m)^6\t%.3f mu m" % (np, c6, blockade))



print("%.2f us : Lifetime of %.0f" % (
10 ** 6 * atom.getStateLifetime(np, 0, 0.5, temperature=0, includeLevelsUpTo=40), np))
print("%.2f us : Lifetime of %.0f" % (
10 ** 6 * atom.getStateLifetime(ni, 0, 0.5, temperature=0, includeLevelsUpTo=40), ni))

print("%.2f us : Lifetime of %.0f with BB" % (
10 ** 6 * atom.getStateLifetime(np, 0, 0.5, temperature=300, includeLevelsUpTo=40), np))
print("%.2f us : Lifetime of %.0f with BB" % (
10 ** 6 * atom.getStateLifetime(ni, 0, 0.5, temperature=300, includeLevelsUpTo=40), ni))


print("%.2f us : Lifetime of %.0f with BB" % (
10 ** 6 * atom.getStateLifetime(69, 0, 0.5, temperature=300, includeLevelsUpTo=80), 69))
print("%.2f us : Lifetime of %.0f with BB" % (
10 ** 6 * atom.getStateLifetime(69, 0, 0.5, temperature=300, includeLevelsUpTo=80), 69))


state1n = 5
state1j = 1.5
state1mj = 1.5

state2n = 67
state2j = 0.5
state2mj = 0.5

dme = atom.getDipoleMatrixElement(state1n, 1, state1j, state1mj, state2n, 2, 1.5, 1.5, 0)
#dme1 = atom.getDipoleMatrixElement(ni, 0, 0.5, 0.5, pstate2n, 1, pstate2j, pstate2mj, 1)

print(dme)

freq = atom.getTransitionFrequency(5, 1, 1.5, 67, 0, 0.5)/2

print("5p-67S", freq/10**12)

freq = atom.getTransitionFrequency(5, 1, 1.5, 56, 0, 0.5)/2

print("5p-56S", freq/10**12)

freq = atom.getTransitionFrequency(5, 1, 1.5, 67, 0, 0.5)/2 - atom.getTransitionFrequency(5, 1, 1.5, 56, 0, 0.5)/2

print("diff", freq/10**12)



freq = atom.getTransitionFrequency(5, 1, 1.5, 67, 2, 0.5)/2

print("5p-67D", freq/10**12)

freq = atom.getTransitionFrequency(69, 0, 0.5, 67, 2, 0.5)

print("69S-67D [GHz]", freq/10**9)


freq = atom.getTransitionFrequency(67, 2, 0.5, 68, 1, 0.5)

print("67D-68P [GHz]", freq/10**9)


freq = atom.getTransitionFrequency(68, 1, 0.5, 66, 2, 0.5)

print("68P-66D [GHz]", freq/10**9)

freq = atom.getTransitionFrequency(66, 2, 0.5, 67, 1, 0.5)

print("66D-67P [GHz]", freq/10**9)

freq = atom.getTransitionFrequency(67, 1, 0.5, 67, 0, 0.5)

print("67P-67S [GHz]", freq/10**9)

freq = atom.getTransitionFrequency(67, 0, 0.5, 65, 2, 2.5)

print("67S - 65D [GHz]", freq/10**9)


freq = atom.getTransitionFrequency(67, 0, 0.5, 66, 1, 0.5)

print("67S - 66P [GHz]", freq/10**9)



dme = atom.getDipoleMatrixElement(67, 0, 0.5, 0.5, 67, 1, 1.5, 0.5, 0)/atom.getDipoleMatrixElement(56, 0, 0.5, 0.5, 56, 1, 0.5, 0.5, 0)

freq = atom.getTransitionFrequency(67, 0, 0.5, 69, 0, 0.5)/2

print("67S - 69S [GHz]", freq/10**9)

print(dme)



freq = atom.getTransitionFrequency(5, 1, 1.5, 68, 0, 0.5)/2

print("5p-68S", freq/10**12)

freq = atom.getTransitionFrequency(5, 1, 1.5, 56, 0, 0.5)/2

print("5p-56S", freq/10**12)

freq = atom.getTransitionFrequency(5, 1, 1.5, 68, 0, 0.5)/2 - atom.getTransitionFrequency(5, 1, 1.5, 56, 0, 0.5)/2

print("diff", freq/10**12)

freq = atom.getTransitionFrequency(69, 1, 1.5, 70, 0, 0.5)

print("69p-70S", freq/10**9)