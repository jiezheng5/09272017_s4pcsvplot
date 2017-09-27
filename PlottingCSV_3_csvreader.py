def CSVplot3():
#{
	from matplotlib import pyplot as plt
	from matplotlib import style
	import numpy as np    
	import csv
	
	freq=[]
	IL=[]
	factor=1000
	
	with open('C:\Users\PythonExercise\_s4pCSVPlot\S3Test.txt', 'r') as csvfile:
		csvreader=csv.reader(csvfile, delimiter='\t') #, quotechar='|')
		for row in csvreader:
			if len(row)!=0:
				freq.append(float(row[0])/factor)
				IL.append(float(row[1]))
				#print(', '.join(row))
	csvfile.close()
	
	plt.plot(freq,IL,label='loaded from S3Test.txt') #color='c', align='center')
	plt.title('Using csv.reader with delimiter')
	plt.ylabel('RL')
	plt.xlabel('freq')
	plt.legend(loc='lower right')
	plt.show()
	
	return
#}
def main():
	CSVplot3()

if __name__ == '__main__':
  main()