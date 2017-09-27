from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np    
import csv,sys,os,time

print time.time()

def CSVplot():
#{
	x=[]
	y=[]
	factor=1000 #Frequency convert from MHz to Ghz

	with open('S3Test.txt', "r") as csvfile:
		csvreader=csv.reader(csvfile) #delimiter=' ', quotechar='|')
		for row in csvreader:
			if len(row)!=0:
				#print 'row: ', row, 'row type: ', type(row), 'row length: ', len(row)
				#print 'row.join(): ', ','.join(row[0].split('\t'))
				x.append(float(row[0].split('\t')[0])/factor)
				y.append(float(row[0].split('\t')[1]))
	csvfile.close()
	
	
	#x=[2,3,4]
	#y=[4,8,10]

	#x2=2*x
	#y2=y

	#pt.bar(x,y,color='c', align='center')
	#plt.bar(x2,y2,color='g', align='center')
	plt.plot(x,y)
	plt.title('Using csv.reader then each row.split')
	plt.ylabel('RL (dB')
	plt.xlabel('Frequency (GHz)')

	plt.show()
	#return
#}

def main():
	CSVplot()

if __name__ == '__main__':
  main()