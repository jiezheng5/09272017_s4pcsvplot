# def CSVplot()
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib import pylab
import numpy as np

style.use('ggplot')

x=[2,3,4]
y=[4,8,10]

x2=2*np.array(x)
print x2
y2=y

plt.bar(x,y,color='c', align='center',label='x')
plt.bar(x2,y2,color='g', align='center',label='x2')
plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend(loc='upper left')

plt.show()