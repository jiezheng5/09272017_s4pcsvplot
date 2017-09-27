def CSVplot4():
#{
	from matplotlib import pyplot as plt
	from matplotlib import style
	import numpy as np    
	import csv
	
	freq=[]
	IL=[]
	factor=1000

	freq,IL=np.loadtxt('C:\Users\PythonExercise\_s4pCSVPlot\S3Test.txt', delimiter='\t', unpack='True')
	plt.plot(freq/factor,IL, label='loaded from S3Test.txt') #color='c', align='center')
	plt.title('return loss using np.loadtxt')
	plt.ylabel('RL')
	plt.xlabel('freq')
	plt.show()
	
	return
#}
def main():
	CSVplot4()

if __name__ == '__main__':
  main()