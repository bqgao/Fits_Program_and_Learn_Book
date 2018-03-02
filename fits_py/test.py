#!/usr/local/bin/python3
#-*-coding:utf-8 -*-
"""list = []  # 构造一个空的列表
# lines = len(file.readlines())     #获取文件的行数
n = 0
with open("/Users/bqgao/Desktop/Python/input.txt", "r") as file:  # 打开文件

    for line in file:
        n += 1  # 计算文件的行数
        print line
        list.append(line.split())  # 将读取到的行添加到列表中, split 按空格分割

print n
for i in range(n):
	print
	for j in range(n):

	    print list[i][j],
# print lines"""

# 装饰器 任意函数的计时器
"""def func_timer(func):
    #程序消耗的时间
    
    def f(*args, **kwargs):  #函数 f 的参数与关键字参数
        import time
        start = time.time()        #time 库函数
        results = func(*args, **kwargs)
        print "Elapsed: %.2fs" % (time.time() - start)
        return results
    
    return f
@func_timer

#快速对数列进行排序运算
def almost_quick_sort(xs):
    #差不多能算是一个快速排列

    # 基准条件 base case
    if xs == []:
        return xs
    # 递归条件 recursive case
    else:
        pivot = xs[0]
        less_than = [x for x in xs[1:] if x <= pivot]
        more_than = [x for x in xs[1:] if x > pivot]
        return almost_quick_sort(less_than) + [pivot] + almost_quick_sort(more_than)

xs = [3,1,4,1,5,9,2,6,5,3,5,9]
print almost_quick_sort(xs)
#程序沉睡时间
def sleepy(msg, sleep=1.0):
    #响应之前沉睡给定的时间
    import time
    time.sleep(sleep)
    print msg

sleepy("Hello", 1.5)
#斐波那契数列与阶乘递归函数
def fac(n):            #阶乘递归
	if n <= 1:
		return 1
	else:
		return n*fac(n-1)

def  fib(n):
	if n < 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)
print fac(6)"""
#权重归一化
"""def normalize(ws):
    #Returns normalized set of weights that sum to 1.
    s = sum(ws)
    return [w/s for w in ws]
ws = [1.0,2.0,3.0,4.0,5.0]
print (normalize(ws))"""
import numpy as np
def var(xs):
    #返回样本数据的方差   $$ s^2 = \frac{\sum_{i=1}^{n} x_i^2 - (\sum_{i=1}^n x_i)^2/n}{n-1} $$
    #求和符号只需要循环即可解决、x*x 的累加与 x 累加的平方
    n = 0
    s = 0
    ss = 0
    
    for x in xs:
        n +=1
        s += x
        ss += x*x

    v = (ss - (s*s)/n)/(n-1)
    return v
# 从方差为1的正态分布中的取出来的数字样本的方差是多少？

np.random.seed(4)
xs = np.random.normal(1e9, 1, 1000)#the random sample of guassin distribution
print (var(xs))
