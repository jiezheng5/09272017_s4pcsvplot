import matplotlib.pyplot as plt
from matplotlib import style
from StringIO import StringIO
import os,sys,time, csv, re,json
import numpy as np    
import pandas as pd
#%matplotlib notebook

def CSVplot8():
	freq=[]
	RL=[]
	factor=1000	
	

	data=pd.read_csv("C:\Users\PythonExercise\_s4pCSVPlot\S4Test.csv",sep='\t', skiprows=0)
	data['VNAResult_split'] = data['VNAResult'].str.split('\t').tolist()

	#print 'header: \n', data.head(),'\n\ncolumn: \n', data.columns,'\n\ndtype: \n', data.dtypes 
	print data['VNAResult_split'][0],data['VNAResult_split'][0][0],data['VNAResult_split'][0][1]
	#data=pandas.read_csv("C:\Users\PythonExercise\S4Test.csv",delimiter="\t",header=False,skiprows=1)
	#data=np.genfromtxt("C:\Users\PythonExercise\S4Test.csv",delimiter="\t",skip_header=1,dtype="U75")
	#print("Data header is: ",data.head(1),"\n")
	#print("Data column name is: ",data.columns,"\n")
	#print("Data size is: ", data.shape,"\n")

		
	for item in data['VNAResult_split']:
		print item, item[0],item[1]
		freq.append(float(item[0])/factor)
		RL.append(float(item[1])/factor)

	plt.figure()
	plt.plot(freq,RL,'r--',label='loaded from S4Test.txt') #color='
	#plt.plot(data['VNAResult_split'][0],data['VNAResult_split'][1],'r--',label='loaded from S4Test.txt') #color='c', align='center')
	plt.title('S4 Return Loss_07/24')
	plt.ylabel('RL (dB)')
	plt.xlabel('Freq (GHz)')
	plt.legend()
	plt.show()	
	return

def main():
	CSVplot8()

if __name__ == '__main__':
	main() 
