from __future__  import print_function
import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
#ax = fig.add_subplot(111)

def onclick(event):
    print(event.xdata)


    print(int(math.floor(event.xdata)))
    
    #print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          #('double' if event.dblclick else 'single', event.button,
          # event.x, event.y, event.xdata, event.ydata))

x_axis = np.arange(7 + 1)
y_axis = np.arange(6 + 1)

for x in range(len(x_axis)):
    line = np.zeros(len(y_axis)) + x
    plt.plot(line, np.arange(len(y_axis)), 'k')

for y in range(len(y_axis)):
    line = np.zeros(len(x_axis)) + y
    plt.plot(np.arange(len(x_axis)), line, 'k')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()



