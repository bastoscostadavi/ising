import ast
import os


model = [0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,1.9,2,2.1,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5]
answer = []
path = 'data/'
files = os.listdir(path)
for file_name in files:
	path = 'data/'+file_name
	data = open(path, 'r')
	T = ast.literal_eval(data.readline())
	X = ast.literal_eval(data.readline())	
	Z = []	
	for k in range(len(T)):		
		if T[k] in model:
			Z += [X[k]]
	data.close()
	words = file_name.split('_')
	data = open(words[0]+'_'+words[1][1:], 'w')
	data.write(str(Z))
