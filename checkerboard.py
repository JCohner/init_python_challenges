from __future__  import print_function
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

fig = plt.figure()
#ax = fig.add_subplot(111)

players = ['p1', 'p2']
turn = 0
def onclick(event):
    #print(event.xdata)
    col = int(math.floor(event.xdata))
    print(df.iloc[-1, col])
    check_df(col, -1)
    print(df)

def check_df(col, row):
    if (active_player == players[0]):
        marker = 1
    elif (active_player == players[1]):
        marker = -1
    
    if(df.iloc[row, col] == 0):
        df.iloc[row, col] = marker
        active_player = players[(turn) + 1 % 2]
    elif (row < -6):
        print("you cant place there")
    else:
        check_df(col, row - 1)
x_axis = np.arange(7 + 1)
y_axis = np.arange(6 + 1)

active_player = players[turn]
print(active_player)
df = pd.DataFrame(np.zeros((8,7))).astype('int32')

for x in range(len(x_axis)):
    line = np.zeros(len(y_axis)) + x
    plt.plot(line, np.arange(len(y_axis)), 'k')

for y in range(len(y_axis)):
    line = np.zeros(len(x_axis)) + y
    plt.plot(np.arange(len(x_axis)), line, 'k')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()



