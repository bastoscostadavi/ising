import numpy as np
import sys
import ast
import matplotlib.pyplot as plt

property = sys.argv[1]

#Temperatures
T = np.array([0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,1.9,2,2.1,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5])

#Reduced temperature
Tc = 2.269
t = (T-Tc)/Tc


lenght = [5,15,20,25]
for l in lenght:
	data = open('data_set_2/'+property+'_%i'%l,'r')
	X = np.array(ast.literal_eval(data.readline()))*l**4
	plt.plot(t,X,label='l=%i'%l)
	#*l**(1/9)
	
plt.grid(True)
plt.legend()
plt.title('Energia interna por temperatura',fontsize=20)
plt.ylabel('Energia interna',fontsize=20)
plt.xlabel('Temperatura',fontsize=20)
plt.show()
