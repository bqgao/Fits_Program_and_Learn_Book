# Draw samples from the distribution:
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sps
mu1=1.0
mu2=2.0 
mu3=3.0# mean=4, std=2*sqrt(2)
#s = np.random.gamma(shape, scale, 1000)

# Display the histogram of the samples, along with
# the probability density function:

#count, bins, ignored = plt.hist(s, 50, normed=True)
bins = np.arange(0,20,0.2)
y1 = bins**(mu1-1)*(np.exp(-bins/2.0) /
                     (sps.gamma(mu1)*2.0**mu1))
y2 = bins**(mu2-1)*(np.exp(-bins/2.0) /
                     (sps.gamma(mu2)*2.0**mu2))
y3 = bins**(mu3-1)*(np.exp(-bins/2.0) /
                     (sps.gamma(mu3)*2.0**mu3))
plt.plot(bins, y1, linewidth=2, color='r',label='n=2')
plt.plot(bins, y2, linewidth=2, color='g',label='n=4')
plt.plot(bins, y3, linewidth=2, color='b',label='n=6')
plt.title("Probability destiny function " r'${\chi_n}^2$')
plt.xlabel('x')
plt.ylabel(r'$f_n(x)$')
plt.legend()
plt.show()