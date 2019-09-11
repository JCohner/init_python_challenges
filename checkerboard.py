from __future__  import print_function
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

fig = plt.figure()
#ax = fig.add_subplot(111)

def onclick(event):
    #print(event.xdata)
    col = int(math.floor(event.xdata))
    print(df.iloc[-1, col])
    if (df.iloc[-1, col] == 0):
        df.iloc[-1, col] = 1
    print(df)
x_axis = np.arange(7 + 1)
y_axis = np.arange(6 + 1)

df = pd.DataFrame(np.zeros((7,6))).astype('int32')

for x in range(len(x_axis)):
    line = np.zeros(len(y_axis)) + x
    plt.plot(line, np.arange(len(y_axis)), 'k')

for y in range(len(y_axis)):
    line = np.zeros(len(x_axis)) + y
    plt.plot(np.arange(len(x_axis)), line, 'k')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()



