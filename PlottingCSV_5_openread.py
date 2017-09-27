def CSVplot5():
#{
	from matplotlib import pyplot as plt
	from matplotlib import style
	import numpy as np    
	import csv
	import re
	
	freq=[]
	IL=[]
	#length=0
	
	'''open().read() a single string while open() a list'''
	path=open('C:\Users\PythonExercise\_s4pCSVPlot\S3Test.txt', "rU")
	data=path.read()
	#rows=data.split("\n","\t")
	#rows=re.split(r'[\n\t]',data)
	rows=re.split(r'\n',data)
	spara=[]
	
	for row in rows:
		#print row
		spara.append(row.split("\t"))
	

	#spara=np.array(spara)	
	print len(spara), len(spara[0]) #np.shape(spara)

	print spara[0], ' and ', spara[-1]
	for item in spara[0:len(spara)-1]:
		#if len(item)!=0:
		#print item
		#print item[-1]
		freq.append(float(item[0]))
		IL.append(float(item[-1]))
		#IL.append(item[1])
		#length=len(item)-1
	
	#print("\n")
	#print(freq[len(freq)-2: len(freq)-1])
	#print(IL[len(IL)-2: len(IL)-1])
	#print(length)
	
	plt.plot(freq,IL,label='loaded from S3Test.txt') #color='c', align='center')
	plt.title('return loss using open().read().split(\n)')
	plt.ylabel('RL')
	plt.xlabel('freq')
	plt.show()
	
	return
#}
def main():
	CSVplot5()

if __name__ == '__main__':
  main()