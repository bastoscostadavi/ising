import numpy as np

def ising(beta,l):
	'''float,int -> float,float,list,list
	given the temperature $\beta = \frac{1}{K_BT}$ and the size l of the system, 
	return the expectation value of the energy and the magnetization, and the array of all E and M obtained in the simulation.
	'''

#generate lattice with cyclic boundary conditions represented by the two extra-layers 
	lattice = np.ones([l+2,l+2])


#calculate initial energy E0 and initial magnetization M0, and built the energy E and magnetization M lists
	M0 = np.sum(lattice)-4*l-4
	E0 = 0
	for i in range(0,l):
		for j in range(0,l):
			sk = lattice[i+1][j+1]
			E0 += sk*lattice[i+2][j+1]+sk*lattice[i+1][j+2]
	E = [-E0]
	M = [M0]


#start monte carlo algorithm where N is the number of monte carlo steps
	N = 500000
	for k in range(N):


#choose ij-spin to invert
		i = np.random.randint(0,l)
		j = np.random.randint(0,l) 


#calculate $$E_\nu-E_\mu=2Js_k^\nu\sum s_i^\mu$$, where the summation is over the nearest neighbors of k
		sk = lattice[i+1][j+1]
		e = 2*sk*(lattice[i+1][j]+lattice[i+1][j+2]+lattice[i][j+1]+lattice[i+2][j+1])


#change the configuration of the lattice
		if e < 0 or np.random.rand() < np.exp(-beta*e):
			E += [E[k]+e]
			M += [M[k]-2*sk]
			lattice[i+1][j+1] = -lattice[i+1][j+1]
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
	

#calculate the expected value of energy and magnetization using $$Q_M=\frac{1}{M}\sum_{n=1}^{M}Q_{\mu_i}$$ using the sampling from the termalization time t onwards, and them calculate the internal energy and the average magnetization per site dividing the result by the number of sites (l**2)	
	t = 18000
	
	return np.mean(np.array(E[-t:]))/l**2,np.mean(np.array(M[-t:]))/l**2,E,M


	




