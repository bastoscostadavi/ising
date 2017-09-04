import numpy as np
import sys
import ast
import matplotlib.pyplot as plt



#Cation, as grandezas, energy, magnetization, foram calculadas não são por partícula. E heat e susceptibility foram calculadas a partir delas, de forma que precisam ser divididas por n para ficar correto.



N = 1000000
data = open('data/energies.txt','r')
N = np.array(range(N+1))
X = ast.literal_eval(data.readline())
plt.plot(N,X)
plt.grid(True)
plt.legend()
plt.title('Energia interna pelo número de passos de Monte Carlo',fontsize=20)
plt.ylabel('Energia interna',fontsize=20)
plt.xlabel('Número de passos de Monte Carlo',fontsize=20)
plt.show()

'''
lenght = [7,9,11,13,15,17,19]
for l in lenght:
	property = sys.argv[1]
	data = open('data_set_4/'+property+'_l'+str(l)+'_N1000000_t250000.txt','r')
	T = np.array(ast.literal_eval(data.readline()))
	X = np.array(ast.literal_eval(data.readline()))/l**2
	plt.plot(T,X,label='N=%i'%int(l)**2)
plt.grid(True)
plt.legend()
plt.title('Susceptibilidade magnética por temperatura',fontsize=20)
plt.ylabel('Susceptibilidade magnética',fontsize=20)
plt.xlabel('Temperatura',fontsize=20)
plt.show()
'''



'''
#For save images of termalization process

for N in [1,10,100,1000,10000,100000,1000000,10000000,100000000-1]:
	file_name = 'data/lattice%i.txt'%N
	lattice = np.loadtxt(file_name)
	plt.imshow(lattice[1:-1,1:-1]
, cmap='Greys',  interpolation='nearest')
	plt.savefig('figures/termalization%i.png'%N)
'''



'''
data = open('data/magnetization.txt','r')
T = ast.literal_eval(data.readline())
X = ast.literal_eval(data.readline())
plt.plot(T,X,'.',color='black')
plt.grid(True)
plt.title('Magnetização por partícula por temperatura',fontsize=20)
plt.ylabel('Magnetização por partícula',fontsize=20)
plt.xlabel('Temperatura',fontsize=20)
plt.ylim([-0.2,1.2])
plt.xlim([0,5])
plt.show()
'''

'''
data = open('data/heat.txt','r')
T = ast.literal_eval(data.readline())
X = ast.literal_eval(data.readline())
plt.plot(T,X,'.',color='black')
plt.grid(True)
plt.title('Capacidade térmica por temperatura',fontsize=20)
plt.ylabel('Capacidade térmica',fontsize=20)
plt.xlabel('Temperatura',fontsize=20)
plt.xlim([0,5])
plt.ylim([-0.0002,0.0016])
plt.show()
'''

'''
data = open('data/susceptibility.txt','r')
T = ast.literal_eval(data.readline())
X = ast.literal_eval(data.readline())
plt.plot(T,X,'.',color='black')
plt.grid(True)
plt.title('Susceptibilidade magnética por temperatura',fontsize=20)
plt.ylabel('Susceptibilidade magnética',fontsize=20)
plt.xlabel('Temperatura',fontsize=20)
plt.xlim([0,5])
plt.ylim([-1,10])
plt.show()
'''
