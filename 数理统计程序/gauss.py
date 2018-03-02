#!/usr/bin/python
#-*-coding:utf-8 -*-
from math import *
from random import *
import matplotlib.pyplot as plt 
import numpy as np 
sum = 0.0
def f(x):
	 f =1.0/1000*1.0/sqrt(2 * pi) * exp(-(x ** 2)/2.0)
	 return f
x = []
y = []
for i in range(1000):
	U1 = uniform(0.0,1.0)
	#U2 = uniform(0.0,1.0)
	#X  = sqrt(-2 * log(U1)) * cos(2 * pi * U2)
	#Y  = sqrt(-2 * log(U1)) * sin(2 * pi * U2)
	x.append(U1)
	#y.append(Y)
X = np.array(x)
for i in X:
	sum = sum + f(i)
	#print i
print("%10.16f" %sum)
print len(X)

#plt.figure(1)
#n, bins, patches = plt.hist(x, 100, normed=1, facecolor='g', alpha=0.75)
#plt.figure(2)
#n, bins, patches = plt.hist(y, 100, normed=2, facecolor='r', alpha=0.75)


#plt.show()	
"""else:
		continue

x = np.array(y)
#np.savetxt("result.txt", x);
file = open("out.text","w")
for i in y:
	file.write(str(i))
	file.write("\n")
file.close()"""

"""with open("out.text","w") as file:
	for i in range(len(x)):
		file.write(x[i])

file.close()"""
"""list = []
for i in range(len(x)):
	a = x[i]
	list.append((f(a)))
    
y = np.array(list)
count, bins, ignored = plt.hist(x, 100, normed=True)
plt.title('Random Gaussian data')
plt.xlabel('variable X (bin size = 0.01)')
plt.ylabel('count')
 
plt.show()"""

    


