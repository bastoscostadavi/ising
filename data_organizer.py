import ast
import os


model = [0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,1.9,2,2.1,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5]
answer = []
path = 'data/'
files = os.listdir(path)
for file_name in files:
	path = 'data/'+file_name
	data = open(path, 'r')
	T1 = ast.literal_eval(data.readline())
	X1 = ast.literal_eval(data.readline())
	T2 = ast.literal_eval(data.readline())
	X2 = ast.literal_eval(data.readline())	
	data.close()
	T = T1 + T2
	X = X1 + X2
	data = open(path, 'w')
	data.write(str(T)+'\n'+str(X))
	data.close()
