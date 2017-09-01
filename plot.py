import numpy as np
import sys
import ast
import matplotlib.pyplot as plt


a = ['energy','magnetization','heat','susceptibility']
k = 3

file_name = sys.argv[1]
data = open(file_name,'r')
T = ast.literal_eval(data.readline())
X = ast.literal_eval(data.readline())
plt.plot(T,X,label='l=%i'%15)
data = open('data/'+a[k]+'_l25_N100000000_t500000.txt','r')
T = ast.literal_eval(data.readline())
X = ast.literal_eval(data.readline())
plt.plot(T,X,label='l=%i'%25)
data = open('data/'+a[k]+'_l20_N100000000_t500000.txt','r')
T = ast.literal_eval(data.readline())
X = ast.literal_eval(data.readline())
plt.plot(T,X,label = 'l=%i'%20)
data = open('data/data_set_1/heat.txt','r')
T = ast.literal_eval(data.readline())
X = ast.literal_eval(data.readline())
plt.plot(T,X,label = 'l=%i'%10)
plt.grid(True)
plt.legend()
plt.title('Energia interna por temperatura',fontsize=20)
plt.ylabel('Energia interna',fontsize=20)
plt.xlabel('Temperatura',fontsize=20)
plt.show()




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
