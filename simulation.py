import numpy as np
import matplotlib.pyplot as plt
from metropolis import ising
 

#define the lattice with cyclic boundary conditions represented by the two extra-layers, the number of monte carlo steps N, the termalization time t, and the range of temperatures
l = 5
lattice = np.ones([l+2,l+2])
N = 500000
t = 250000
#temperatures = np.array(range(2,52,2))/10
temperatures = [2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5]

energies = []
specific_heats = []
magnetizations = []
magnetic_susceptibilities = []

#notice that we use the lattice earned from the early simulation as the lattice for the next one. This procedure puts down the termalization time.
for temperature in temperatures:
	energy,magnetization,specific_heat,magnetic_susceptibility,lattice = ising(1/temperature,N,t,lattice)[:5]
	energies += [energy]
	magnetizations += [magnetization]
	specific_heats += [specific_heat]
	magnetic_susceptibilities += [magnetic_susceptibility]
file = open('data/energy_l%i_N%i_t%i.txt'%(l,N,t),'a')
file.write(str(temperatures)+' '+str(energies)+'\n')
file.close()	
file = open('data/magnetization_l%i_N%i_t%i.txt'%(l,N,t),'a')
file.write(str(temperatures)+' '+str(magnetizations)+'\n')
file.close()	
file = open('data/heat_l%i_N%i_t%i.txt'%(l,N,t),'a')
file.write(str(temperatures)+' '+str(specific_heats)+'\n')
file.close()	
file = open('data/susceptibility_l%i_N%i_t%i.txt'%(l,N,t),'a')
file.write(str(temperatures)+' '+str(magnetic_susceptibilities)+'\n')
file.close()	

