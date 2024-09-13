import numpy as np
import matplotlib.pyplot as plt
n = 101
x = np.linspace(0,10,n)
y_exp = np.exp(-0.3*x)
y_noise = y_exp + 0.7*(np.random.random(n)-0.5)

max_noise = y_exp
condition = (y_noise - max_noise)
X = x[y_noise>0]
y_noise = y_noise[y_noise>0]




y_noise_log = np.log(y_noise)
data = np.polyfit(X,y_noise_log,deg=1)

logy = data[1] + data[0]*X
plt.plot(x, y_exp, X, np.exp(logy))
plt.show()