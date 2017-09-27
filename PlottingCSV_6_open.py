def CSVplot6():
#{
	from matplotlib import pyplot as plt
	from matplotlib import style
	import pylab
	import numpy as np    
	import csv
	import re
	
	freq=[]
	RL=[]
	factor=1000	
	
	path=open("C:\Users\PythonExercise\_s4pCSVPlot\S3Test.txt", "r")
	#data=path.read()
	#rows=re.split(r'[\n]',data)
	spara=[]
	
	for line in path:
		spara.append(line.rstrip('\n').split("\t"))
			
	for item in spara[0:len(spara)]:
		#print item
		#print(item[0])
		#print(type(item[0]))
		#print(float(item[0])/factor)
		freq.append(float(item[0])/factor)
		#IL.append( (item[len(item)-1]) /factor)
		RL.append(float(item[1])/1)
			
	pylab.plot(freq,RL,"r--",label='loaded from S3Test.txt') #color='c', align='center')
	pylab.title('Return Loss using open() and rstrip()')
	pylab.ylabel('RL (dB)')
	pylab.xlabel('Freq (GHz)')
	pylab.legend()
	pylab.show()
	
	return
#}
def main():
	CSVplot6()

if __name__ == '__main__':
  main()