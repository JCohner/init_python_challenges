from __future__  import print_function
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from termcolor import cprint


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
        self.win_check(col, row)
        pos = (col + 0.5 ,abs(row) - 0.5)
        #print(pos)
        if (marker == 1):
            color = 'r'
        elif (marker == -1):
            color = 'b'
        circle = plt.Circle(pos, 0.4, color = color)
        self.ax.add_artist(circle)
        plt.show()
   
    def win_check(self, col, row):
        #col_win()
        win_col_1 = (self.df.iloc[:, col] == 1)
        win_col_2 = (self.df.iloc[:, col] == -1)

        win_col_1_counts = win_col_1.value_counts()
        win_col_2_counts = win_col_2.value_counts()

        if (len(win_col_1_counts.index) > 1):
            num_pieces = win_col_1_counts.loc[True]
            print("player 1 has " + str(num_pieces) + " pieces in this col")
            if (num_pieces >= 4):
                print(win_col_1)
                seq = 0
                x = 0
                while x < len(win_col_1) and seq < 4 :
                    if (win_col_1[x] == True):
                        seq = seq + 1
                    else:
                        seq = 0
                    x = x + 1
                if (seq >= 4):
                    cprint("player 1 wins!", 'red')

        if (len(win_col_2_counts.index) > 1):
            num_pieces = win_col_2_counts.loc[True]
            print("player 2 has " + str(num_pieces) + " pieces in this col")
            if (num_pieces >= 4):
                print(win_col_2)
                seq = 0
                x = 0
                while x < len(win_col_2) and seq < 4 :
                    if (win_col_2[x] == True):
                        seq = seq + 1
                    else:
                        seq = 0
                    x = x + 1
                if (seq >= 4):
                    cprint("player 2 wins!", 'blue')      

        #row_win()
        win_row_1 = (self.df.iloc[row, :] == 1)
        win_row_2 = (self.df.iloc[row, :] == -1)

        win_row_1_counts = win_row_1.value_counts()
        win_row_2_counts = win_row_2.value_counts()

        if (len(win_row_1_counts.index) > 1):
            num_pieces = win_row_1_counts.loc[True]
            print("player 1 has " + str(num_pieces) + " pieces in this row")
            if (num_pieces >= 4):
                print(win_row_1)
                seq = 0
                x = 0
                while x < len(win_row_1) and seq < 4 :
                    if (win_row_1[x] == True):
                        seq = seq + 1
                    else:
                        seq = 0
                    x = x + 1
                if (seq >= 4):
                    cprint("player 1 wins!", 'red')

        if (len(win_row_2_counts.index) > 1):
            num_pieces = win_row_2_counts.loc[True]
            print("player 2 has " + str(num_pieces) + " pieces in this row")
            if (num_pieces >= 4):
                print(win_row_2)
                seq = 0
                x = 0
                while x < len(win_row_2) and seq < 4 :
                    if (win_row_2[x] == True):
                        seq = seq + 1
                    else:
                        seq = 0
                    x = x + 1
                if (seq >= 4):
                    cprint("player 2 wins!", 'blue')      
        #diag_win()
        total_seq = self.diag_win_check(col, row, [])
        print(total_seq)

    def diag_win_check(self, col, row, checked):
        num_diag = 0
        print((row, col))
        pos_slope_neighbors = []
        neg_slope_neighbors = []
        for x in range(-1,2,2):
            for y in range(-1,2,2):
                if ((row + x) < 0) and ((col + y) >= 0):
                    print("checking coord " + str((row+x,col+y)))
                    print(self.df.iloc[row + x, col + y])
                    if (self.df.iloc[row + x, col + y] == 1):
                        print("got a hit at")
                        print(str((row + x, col + y)))
                        print((x,y))
                        if ((x * y) < 0): #means they are of the same sign
                            pos_slope_neighbors.append((row+x, col+y))
                        elif ((x * y) > 0): #means they are of opposite sign
                            neg_slope_neighbors.append((row+x, col+y))
        print("checked is")
        checked.append((row,col))
        print(checked)

        #pos slope neighbor check
        recurse_sum = 1
        #print("positive sloping neighbors are " + str(pos_slope_neighbors))
        for x in range(len(pos_slope_neighbors)):
            #print(pos_slope_neighbors[x])
            if (pos_slope_neighbors[x] not in checked):
                print("Calling recursion!")
                recurse_sum = recurse_sum  + self.diag_win_check(pos_slope_neighbors[x][1], pos_slope_neighbors[x][0], checked)
       
        recurse_sum_b = 1
        for x in range(len(neg_slope_neighbors)):
            #print(pos_slope_neighbors[x])
            if (neg_slope_neighbors[x] not in checked):
                print("Calling recursion!")
                recurse_sum_b = recurse_sum_b  + self.diag_win_check(neg_slope_neighbors[x][1], neg_slope_neighbors[x][0], checked)

        #print(recurse_sum)
        return recurse_sum



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


