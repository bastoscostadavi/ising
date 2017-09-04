import numpy as np

def ising(beta,N,t,lattice):
	'''float,int,int,int -> float,float,,float,float,list,list
	given the temperature $\beta = \frac{1}{K_BT}$, the number of monte Carlo Steps, the termalization time measured in monte Carlo Steps and the size l of the system, 
	return the expectation value of the energy and the magnetization and the expectation value of the square of this quantities, and the array of all E and M obtained during the simulation.
	'''

#calculate initial energy E0 and initial magnetization M0, and built the energy E and magnetization M lists
	l = len(lattice)-2
	M0 = np.sum(lattice[1:l+1,1:l+1])
	E0 = 0
	for i in range(0,l):
		for j in range(0,l):
			sk = lattice[i+1][j+1]
			E0 += sk*lattice[i+2][j+1]+sk*lattice[i+1][j+2]
	E = [-E0]
	M = [M0]


#start monte carlo algorithm where N is the number of monte carlo steps
	for k in range(N):

#choose ij-spin to invert
		i = np.random.randint(0,l)
		j = np.random.randint(0,l) 


#calculate $$E_\nu-E_\mu=2Js_k^\nu\sum s_i^\mu$$, where the summation is over the nearest neighbors of k
		sk = lattice[i+1][j+1]
		e = 2*sk*(lattice[i+1][j]+lattice[i+1][j+2]+lattice[i][j+1]+lattice[i+2][j+1])


#decide whether change the configuration of the lattice
		if e < 0 or np.random.rand() < np.exp(-beta*e):
			E += [E[k]+e]
			M += [M[k]-2*sk]
			lattice[i+1][j+1] = -lattice[i+1][j+1]

#this part deals with the fact that the lattice is ciclic and have two extra layers.
			if i == 0:
				lattice[l+1][j+1] = lattice[i+1][j+1]
			if i == l-1:
				lattice[0][j+1] = lattice[i+1][j+1]
			if j == 0:
				lattice[i+1][l+1] = lattice[i+1][j+1]
			if j == l-1:
				lattice[i+1][0] = lattice[i+1][j+1]
		else:
			E += [E[k]]
			M += [M[k]]


#Calculate the average energy, the average magnetization, the specific heat and the magnetic susceptibility	
	energy_sampling = np.array(E[-t:])
	magnetization_sampling = np.array(M[-t:])
	average_energy = np.mean(energy_sampling)
	average_magnetization = np.mean(np.abs(magnetization_sampling))
	specific_heat = (beta**2)*(np.mean(energy_sampling**2)-average_energy**2)
	magnetic_susceptibility = (beta)*(np.mean(magnetization_sampling**2)-average_magnetization**2)

	return average_energy,average_magnetization,specific_heat,magnetic_susceptibility,lattice,E,M


	




