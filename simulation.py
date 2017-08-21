import numpy as np
import matplotlib.pyplot as plt
from metropolis import ising


#the values of lenght are the values of l for which the simulation will be made
l = 5
#the values of temperatures are the values of the temperature for which the simulation will be made
temperatures = np.array(range(2,52,2))/10

energy = []
magnetization = []
for T in temperatures:
	e,m,E,M = ising(1/T,l)
	energy += [e]
	magnetization += [m]
	file = open('data/energy_termalization.txt','a')
	file.write(str(E)+'\n')
	file.close()		
	file = open('data/magnetization_termalization.txt','a')
	file.write(str(M)+'\n')
	file.close()		
file = open('data/energy.txt','a')
file.write(str(energy)+'\n')
file.close()	
file = open('data/magnetization.txt','a')
file.write(str(magnetization)+'\n')
file.close()

