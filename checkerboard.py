from __future__  import print_function
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd


#ax = fig.add_subplot(111)


class Game():
    def check_df(self, col, row):
        if (self.active_player == self.players[0]):
            marker = 1
        elif (self.active_player == self.players[1]):
            marker = -1
        
        if(self.df.iloc[row, col] == 0):
            self.df.iloc[row, col] = marker
            self.turn = (self.turn + 1) % 2
            self.active_player = self.players[self.turn]
            print(self.active_player)
            self.make_circle(col, row, marker)
        elif (row < -7):
            print("you cant place there")
        else:
            self.check_df(col, row - 1)

    def make_circle(self, col, row, marker):
        pos = (col + 0.5 ,abs(row) - 0.5)
        print(pos)
        if (marker == 1):
            color = 'r'
        elif (marker == -1):
            color = 'b'
        circle = plt.Circle(pos, 0.5, color = color)
        self.ax.add_artist(circle)
        plt.show()

    def onclick(self, event):
            #print(self.active_player)
            col = int(math.floor(event.xdata))
            
            print(self.df.iloc[-1, col])
            self.check_df(col, -1)
            print(self.df)

    def __init__(self):
        self.num_rows = 7 + 1
        self.num_columns = 6 +1
        self.df = pd.DataFrame(np.zeros((self.num_rows,self.num_columns))).astype('int32')
        print(self.df)
        

        fig, self.ax = plt.subplots()
        x_axis = np.arange(self.num_rows)
        y_axis = np.arange(self.num_columns)
        for x in range(len(x_axis)):
            line = np.zeros(len(y_axis)) + x
            plt.plot(line, np.arange(len(y_axis)), 'k')

        for y in range(len(y_axis)):
            line = np.zeros(len(x_axis)) + y
            plt.plot(np.arange(len(x_axis)), line, 'k')
        cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
        

        self.players = ['p1', 'p2']
        self.turn = 0
        self.active_player = self.players[self.turn]
        print(self.active_player)
        plt.show()


g = Game()


