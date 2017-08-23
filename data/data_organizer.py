import os
import sys

paths = ["data/energy","data/magnetization","data/susceptibility","data/heat"]
for path in paths:
	simulations = os.listdir(path)
	data = {}
	N_list = []
	for simulation in simulations:
		key = 0
		N = ''
		for character in simulation:
			if character == "_":
				key = 0 
			if key == 1:
				N += character 		
			if character == "N":
				key = 1	
		N_list += [float(N)]
	ordered_simulations = [x for _,x in sorted(zip(N_list,simulations))]
	for simulation in ordered_simulations:	
		file = open(path+'/'+simulation, 'r')
		lines = file.readlines()
		for line in lines:
			
			print(w)
