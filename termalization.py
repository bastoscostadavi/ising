import numpy as np
import matplotlib.pyplot as plt
from metropolis import ising
 


#define the lattice with cyclic boundary conditions represented by the two extra-layers, the number of monte carlo steps N, the termalization time t, and the range of temperatures


l = 20
N = 1000000
t = 250000
temperature = 10
lattice = np.ones([l+2,l+2])
energies = ising(1/temperature,N,t,lattice)[5]
file = open('data/energies.txt','a')
file.write(str(energies))
file.close()	
