def CSVplot7():

	from matplotlib import pyplot as plt
	from matplotlib import style
	from StringIO import StringIO
	import numpy as np    
	import csv
	import re
	
	freq=[]
	RL=[]
	factor=1000	
	
	#vector = np.array(["1", "2", "3"])
	#print(type(vector[0]))
	#vector = vector.astype(float)
	#print(type(vector[0]),"\n")
    
	data=np.genfromtxt("C:\Users\PythonExercise\_s4pCSVPlot\S4Test.csv",delimiter="\n", skip_header=1,dtype="U75")
	print data, data[0] #.astype(float)
	#print(data[:,0],type(data[:,0]))    
	#path=open("C:\Users\PythonExercise\S3Test.csv", "r")
	#data=path.read()
	#rows=data.split("\n","\t")
	#rows=re.split(r'[\n\t]',data)
	#rows=re.split(r'[\n]',data)
	#data=data.astype(float)
	spara=[]
	
	for row in data:
		print row.split('\t')
		spara.append(row.split('\t'))
			
	for item in spara[0:len(spara)-1]:
		#print(item[0])
		#print(type(item[0]))
		#print(float(item[0])/factor)
		freq.append(float(item[0]))
		#freq.append(float(item[0])/factor)
		#IL.append( (item[len(item)-1]) /factor)
		#RL.append(float(item[1])/1)
		RL.append(float(item[1]))
	#plt.plot(freq,RL,label='loaded from S3Test.txt') #color='c', align='center')
	plt.title('S4 Return Loss_06/22')
	plt.ylabel('RL (dB) using np.genfromtxt')
	plt.xlabel('Freq (GHz)')
	plt.show()
	#return

def main():
	CSVplot7()

if __name__ == '__main__':
  main()
