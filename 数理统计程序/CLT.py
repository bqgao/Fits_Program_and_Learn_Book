#!/usr/local/bin/python3
#-*-coding:utf-8 -*-
"""from scipy.stats import expon
from random import *
import numpy as np
import matplotlib.pyplot as plt

data = [47,10,31,25,20,  
        2,11,31,25,21,  
        44,14,15,26,21,  
        41,14,16,26,21,  
        7,30,17,27,24,  
        6,30,17,27,24,  
        35,32,15,29,23,  
        38,33,19,28,20,  
        35,34,18,29,21,  
        36,32,16,27,20]  
a,b = np.histogram(data,bins=[0,5,10,15,20,25,30,35,40,45,50])  
print a  
print b  
print np.max(data),np.mean(data),np.median(data)
plt.scatter(np.array(a),np.array(b),'ro')
plt.show()"""

#xs = np.random.randint(0,10,(5,12)).tolist()  #random 随机库中的 randint 生成随机
#正整数，形式为(low,high,size,type)，上式中生成0-10的5行12列的数组，tolist 将数组转换为列表
from math import *
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn import datasets, linear_model 
import statsmodels.api as sm
#数据预处理
"""data = pd.read_csv('shuju.csv')
x = np.array(data[['v']])
M= np.array(data[['r']])	#绝对星等
y_error = np.array(data[['errbar']])
Velocity = []
yrr = []
for i in x:
	Velocity.append(np.log(i))

for i in y_error:
	yrr.append((np.log(i)))

velocity = np.array(Velocity)	#弥散速度
y_errorbar = np.array(yrr)	#弥散速度误差
"""

data=np.loadtxt("data.txt")
a=data
h=73
z=np.linspace(0,0,32)
g=np.linspace(0,0,32)
v=np.linspace(0,0,32)
verr=np.linspace(0,0,32)
for i in range(32):
    z[i]=a[i,7]
    g[i]=a[i,3]
    v[i]=a[i,0]
    verr[i]=a[i,1]
    
d=np.linspace(0,0,32)
m=np.linspace(0,0,32)
t=np.linspace(0,0,32)
b=np.linspace(0,0,32)
for i in range(32):
    d[i]=(300000*z[i])/h
    t[i]=g[i]+5
    l=d[i]/100
    b[i]=np.log(l)
    m[i]=t[i]-5*(b[i]+8)
coef = np.cov(v,m)[0][1]/(np.std(v)*np.std(m))
print   (coef) 
m = m.reshape(32,1)
v = v.reshape(32,1)

#预测拟合模型

model = linear_model.LinearRegression()
model.fit(v,m)   #linear fit
#predict_outcome = model.predict(predict_value)
fit_result = {}
fit_result['intercept'] = model.intercept_  #截距
fit_result['coefficient'] = model.coef_		#系数
#fit_result['predict_value'] = predict_outcome
print (model.score(v,m))  #模型检验、普通最小二乘法，R-Square
print  (fit_result)

xerr = verr
#图形绘制
def linear_model_picture(x,y):
	model = linear_model.LinearRegression()
	model.fit(x,y)
	plt.grid(True)	#显示网格
	plt.scatter(x,y,color = 'b')
	plt.errorbar(x,y,xerr=verr,fmt='o',color='black',ecolor = 'lightgray',elinewidth =3,capsize = 0)
	plt.plot(x,model.predict(x),'r',linewidth = 4)
	plt.title('Tully-Fisher  g-band')
	plt.xlabel('Diffusion velocity')
	plt.ylabel(' Absolute M')
	plt.ylim(-10.0 -30.0)
	plt.show()


linear_model_picture(v,m)

#计算均方差误差评估模型
est = sm.OLS(m,v)
result = est.fit()
print (result.summary())









