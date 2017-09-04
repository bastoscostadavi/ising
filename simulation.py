import numpy as np
import matplotlib.pyplot as plt
from metropolis import ising
 


#define the lattice with cyclic boundary conditions represented by the two extra-layers, the number of monte carlo steps N, the termalization time t, and the range of temperatures


lenght = [16,17,18,19,20]
N = 1000000
t = 250000
for l in lenght:
	lattice = np.ones([l+2,l+2])
	temperatures = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8, 2.85, 2.9, 2.95, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 5.6, 5.8, 6, 6.2, 6.4, 6.6, 6.8, 7, 7.2, 7.4, 7.6, 7.8, 8]

	energies = []
	specific_heats = []
	magnetizations = []
	magnetic_susceptibilities = []

#notice that we use the lattice earned from the early simulation as the lattice for the next one. This procedure puts down the termalization time.
	file = open('data/energy_l%i_N%i_t%i.txt'%(l,N,t),'a')
	file.write(str(temperatures)+'\n')
	file.close()
	file = open('data/magnetization_l%i_N%i_t%i.txt'%(l,N,t),'a')
	file.write(str(temperatures)+'\n')
	file.close()	
	file = open('data/heat_l%i_N%i_t%i.txt'%(l,N,t),'a')
	file.write(str(temperatures)+'\n')
	file.close()	
	file = open('data/susceptibility_l%i_N%i_t%i.txt'%(l,N,t),'a')
	file.write(str(temperatures)+'\n')
	file.close()

	for temperature in temperatures:
		energy,magnetization,specific_heat,magnetic_susceptibility,lattice = ising(1/temperature,N,t,lattice)[:5]
		energies += [energy]
		magnetizations += [magnetization]
		specific_heats += [specific_heat]
		magnetic_susceptibilities += [magnetic_susceptibility]
	file = open('data/energy_l%i_N%i_t%i.txt'%(l,N,t),'a')
	file.write(str(energies)+'\n')
	file.close()	
	file = open('data/magnetization_l%i_N%i_t%i.txt'%(l,N,t),'a')
	file.write(str(magnetizations)+'\n')
	file.close()	
	file = open('data/heat_l%i_N%i_t%i.txt'%(l,N,t),'a')
	file.write(str(specific_heats)+'\n')
	file.close()	
	file = open('data/susceptibility_l%i_N%i_t%i.txt'%(l,N,t),'a')
	file.write(str(magnetic_susceptibilities)+'\n')
	file.close()	
