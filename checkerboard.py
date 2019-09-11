from __future__  import print_function
import matplotlib.pyplot as plt
import numpy as np

plt.plot()
x_axis = np.arange(7)
y_axis = np.arange(6)

for x in range(len(x_axis)):
    line = np.zeros(len(y_axis)) + x
    plt.plot(line, np.arange(len(y_axis)), 'k')

for y in range(len(y_axis)):
    line = np.zeros(len(x_axis)) + y
    plt.plot(np.arange(len(x_axis)), line, 'k')

plt.show()

