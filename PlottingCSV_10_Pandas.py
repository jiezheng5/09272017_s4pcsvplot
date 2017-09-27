import matplotlib.pyplot as plt
from matplotlib import style
from StringIO import StringIO
import os,sys,time, csv, re,json
import numpy as np    
import pandas as pd
#%matplotlib notebook

def CSVplot10():
	#freq=[]
	#RL=[]
	factor=1000	
	

	data=pd.read_csv("C:\Users\PythonExercise\_s4pCSVPlot\S4Test.csv",sep='\t', skiprows=0)
	#split one column into 2 columns
	newdata= pd.DataFrame(data['VNAResult'].str.split('\t').tolist(),columns=['freq','RL'])
	#newdata= pd.DataFrame(data['VNAResult'].split('\t').tolist(),columns=['freq','RL'])

	plt.figure()
	#plt.plot(freq,RL,'r--',label='loaded from S4Test.txt') #color='
	plt.plot(newdata['freq'].apply(lambda x: float(x)/factor),newdata['RL'],'r--',label='loaded from S4Test.txt') #color='c', align='center')
	plt.title('S4 Return Loss_07/24 using Pandas')
	plt.ylabel('RL (dB)')
	plt.xlabel('Freq (GHz)')
	plt.legend()
	plt.savefig("RL of S4Test.png")
	plt.show()	
	return

def main():
	CSVplot10()

if __name__ == '__main__':
	main() 
