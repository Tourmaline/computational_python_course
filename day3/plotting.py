import matplotlib.pyplot as plt
import numpy as np

datax = np.linspace(0, 1, 8)
datay = [1, 4, 6, 8, 3, 5, 9, 2]

plt.figure(1)
plt.plot(datax, datay)

plt.figure(2)
plt.plot(datax, datay)
plt.show()