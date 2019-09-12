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
                    self.game_state = 1
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
                    self.game_state = -1
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
                    self.game_state = 1
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
                    self.game_state = -1
                    cprint("player 2 wins!", 'blue')      
        #diag_win()
        if (self.active_player == self.players[0]):
            marker = -1 #player 2 is actually going, i must be updating active player at worong point TODO: fix this
        elif (self.active_player == self.players[1]):
            marker = 1

        total_seq_1 = self.pos_diag_win_check(col, row, [], marker)
        print("positive slope total " + str(total_seq_1))

        total_seq_2 = self.neg_diag_win_check(col, row, [], marker)
        print("neg slope total " + str(total_seq_2))

        if (total_seq_1 >= 4 or total_seq_2 >= 4):
            if (self.active_player == self.players[0]):
                cprint("player 2 wins!", 'blue')
                self.game_state = -1
            elif (self.active_player == self.players[1]):
                cprint("player 1 wins!", 'red')
                self.game_state = 1
    #     self.win_print()

    # def win_print(self):
    #     if(self.game_state == 1):
    #         plt.text(3.5, 3, "Player 1 Wins!")
    #         plt.show()
    #     elif (self.game_state == -1):
    #         plt.text(3.5, 3, "Player 2 Wins!")
    #         plt.show()

    def pos_diag_win_check(self, col, row, checked, player):
        print((row, col))
        pos_slope_neighbors = []
        
        for x in range(-1,2,2):
            for y in range(-1,2,2):
                if ((row - x) < 0) and ((col + y) < 7 and (x * y > 0)): #in bounds and positive slope vals
                    print("checking coord " + str((row-x,col+y)))
                    print(self.df.iloc[row - x, col + y])
                    if (self.df.iloc[row - x, col + y] == player):
                        print("got a hit at")
                        print(str((row - x, col + y)))
                        print((x,y))
                        pos_slope_neighbors.append((row-x, col+y))
                        
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
                recurse_sum = recurse_sum  + self.pos_diag_win_check(pos_slope_neighbors[x][1], pos_slope_neighbors[x][0], checked, player)
        print("pos slope recurse sum " + str(recurse_sum))
        return recurse_sum

    def neg_diag_win_check(self, col, row, checked, player):
        print((row, col))
        neg_slope_neighbors = []
        
        for x in range(-1,2,2):
            for y in range(-1,2,2):
                if ((row - x) < 0) and ((col + y) < 7 and (x * y < 0)): #in bounds and negitive slope vals
                    print("checking coord " + str((row-x,col+y)))
                    print(self.df.iloc[row - x, col + y])
                    if (self.df.iloc[row - x, col + y] == player):
                        print("got a hit at")
                        print(str((row - x, col + y)))
                        print((x,y))
                        neg_slope_neighbors.append((row-x, col+y))
                        
        print("checked is")
        checked.append((row,col))
        print(checked)

        #neg slope neighbor check
        recurse_sum = 1
        #print("negitive sloping neighbors are " + str(neg_slope_neighbors))
        for x in range(len(neg_slope_neighbors)):
            #print(neg_slope_neighbors[x])
            if (neg_slope_neighbors[x] not in checked):
                print("Calling recursion!")
                recurse_sum = recurse_sum  + self.neg_diag_win_check(neg_slope_neighbors[x][1], neg_slope_neighbors[x][0], checked, player)
        print("neg slope recurse sum " + str(recurse_sum))
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
        self.game_state = 0
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


