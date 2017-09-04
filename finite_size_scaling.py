import numpy as np
import sys
import ast
import matplotlib.pyplot as plt

property = sys.argv[1]

#Temperatures


lenght = [7,9,11,13,15,17]
for l in lenght:
	data = open('data_set_4/' + property + '_l%i_N1000000_t250000.txt'%l,'r')
	T = np.array(ast.literal_eval(data.readline()))
	Tc = 2.269
	t = (T-Tc)/Tc
	X = np.array(ast.literal_eval(data.readline()))/l**2
	plt.subplot(211)
	plt.plot(t,X,'.',label='N=%i'%l**2)
	plt.ylabel('Calor Específico',fontsize=20)
	plt.xlabel('Temperatura reduzida',fontsize=20)	
	plt.legend()
	plt.subplot(212)
	plt.plot(t*l,X,'.',label='N=%i'%l**2)
	plt.ylabel('Scaling Function',fontsize=20)
	plt.xlabel('Temperatura reduzida',fontsize=20)
	plt.legend()
plt.show()


'''Plot magnetization and magnetization scaling function
lenght = [7,9,11,13,15,17]
for l in lenght:
	data = open('data_set_4/' + property + '_l%i_N1000000_t250000.txt'%l,'r')
	T = np.array(ast.literal_eval(data.readline()))
	Tc = 2.269
	t = (T-Tc)/Tc
	X = np.array(ast.literal_eval(data.readline()))/l**2
	plt.subplot(211)
	plt.plot(t,X,label='N=%i'%l**2)
	plt.xlim((-0.4,1))
	plt.ylabel('Magnetização',fontsize=20)
	plt.xlabel('Temperatura reduzida',fontsize=20)	
	plt.legend()
	plt.subplot(212)
	plt.plot(t*l,X*l**(1/8),label='N=%i'%l**2)
	plt.xlim((-6,6))
	plt.ylabel('Scaling Function',fontsize=20)
	plt.xlabel('Temperatura reduzida',fontsize=20)
	plt.legend()
plt.show()
'''

'''Plot susceptibility and susceptibility scaling function:
lenght = [7,9,11,13,15,17]
for l in lenght:
	data = open('data_set_4/' + property + '_l%i_N1000000_t250000.txt'%l,'r')
	T = np.array(ast.literal_eval(data.readline()))
	Tc = 2.269
	t = (T-Tc)/Tc
	X = np.array(ast.literal_eval(data.readline()))/l**2
	plt.subplot(211)
	plt.plot(t[10:40],X[10:40],'.',label='N=%i'%l**2)
	plt.xlim((-0.2,0.3))	
	plt.ylabel('Susceptibilidade',fontsize=20)
	plt.xlabel('Temperatura reduzida',fontsize=20)	
	plt.legend()
	plt.subplot(212)
	plt.plot(t[10:40]*l,X[10:40]*l**(-7/4),'.',label='N=%i'%l**2)
	plt.xlim((-2,4))
	plt.ylabel('Scaling Function',fontsize=20)
	plt.xlabel('Temperatura reduzida',fontsize=20)
	plt.legend()
plt.show()
'''
