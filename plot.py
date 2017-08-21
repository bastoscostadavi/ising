import numpy as np
import sys
import ast
import matplotlib.pyplot as plt

file_name = sys.argv[1]
l = 5
data = open(file_name,'r')
N = np.array(range(500001))
T = np.array(range(2,52,2))/10
X = ast.literal_eval(data.readlines()[0])
plt.plot(T,X,'.',label='n=%ix%i'%(l,l))
plt.title('Magnetização por partícula por temperatura',fontsize=20)
plt.ylabel('Magnetização por partícula',fontsize=20)
plt.xlabel('Temperatura',fontsize=20)
plt.legend()
plt.show()
