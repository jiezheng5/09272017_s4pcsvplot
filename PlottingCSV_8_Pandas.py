def CSVplot8():

	from matplotlib import pyplot as plt
	from matplotlib import style
	from StringIO import StringIO
	import numpy as np    
	import pylab
	import pandas
	import csv
	import re
	
	freq=[]
	RL=[]
	factor=1000	
	

	data=pandas.read_csv("C:\Users\PythonExercise\S4Test.csv",sep='\t', skiprows=0)
	#data=pandas.read_csv("C:\Users\PythonExercise\S4Test.csv",delimiter="\t",header=False,skiprows=1)
	#data=np.genfromtxt("C:\Users\PythonExercise\S4Test.csv",delimiter="\t",skip_header=1,dtype="U75")
	print("Data header is: ",data.head(1),"\n")
	print("Data column name is: ",data.columns,"\n")
	print("Data size is: ", data.shape,"\n")
	#print("Data is \n" ,data)
	#data[:,0].astype(float)
	#print(data[:,0],type(data[:,0]))    
	#path=open("C:\Users\PythonExercise\S3Test.csv", "r")
	#data=path.read()
	#rows=data.split("\n","\t")
	#rows=re.split(r'[\n\t]',data)
	#rows=re.split(r'[\n]',data)
	spara=[]
	
	for row in data[1:len(data)]:
		spara.append(row)
			
	for item in spara[0:len(spara)-1]:
		#print(item[0])
		#print(type(item[0]))
		#print(float(item[0])/factor)
		#freq.append(item[0])
		freq.append(item[0]/factor)
		#IL.append( (item[len(item)-1]) /factor)
		#RL.append(float(item[1])/1)
		RL.append(item[1])
	plt.plot(freq,RL,'r--',label='loaded from S4Test.txt') #color='c', align='center')
	plt.title('S4 Return Loss_06/30')
	plt.ylabel('RL (dB)')
	plt.xlabel('Freq (GHz)')
	plt.legend()
	plt.show()
	
	return
