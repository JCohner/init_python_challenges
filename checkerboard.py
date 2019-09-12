from __future__  import print_function
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from termcolor import cprint

plt.ion()  

#ax = fig.add_subplot(111)
class Game():
    def check_df(self, col, row):
        if(self.df.iloc[row, col] == 0):
            self.df.iloc[row, col] = self.active_player[2]
            self.make_circle(col, row)
            self.win_check(col, row)
            self.next_player() 
        elif (row < -7):
            print("you cant place there")
            self.prompt_player("you can't place there!", 'k')
        else:
            self.check_df(col, row - 1) #some beautiful recursion if i say so myself

    def make_circle(self, col, row):
        pos = (col + 0.5 ,abs(row) - 0.5)
        circle = plt.Circle(pos, 0.4, color = self.active_player[1])
        self.ax.add_artist(circle)
        plt.show()

   
    def win_check(self, col, row):
        #col win check
        win_col = (self.df.iloc[:, col] == self.active_player[2])
        win_col_counts = win_col.value_counts()

        if (len(win_col_counts.index) > 1):
            num_pieces = win_col_counts.loc[True]
            print(self.active_player[0] + " has " + str(num_pieces) + " pieces in this col")

            if (num_pieces > 3):
                seq = 0
                x = 0
                print("checking if they're seq")
                while x < len(win_col) and seq < 4 :
                    if (win_col[x] == True):
                        seq = seq + 1
                    else:
                        seq = 0
                    x = x + 1
                if (seq >= 4):
                    self.game_state = 1 #TODO: have this stop the game, maybe offer reset
                    self.win_print()

        #row win check
        win_row = (self.df.iloc[row, :] == self.active_player[2])
        win_row_counts = win_row.value_counts()

        if (len(win_row_counts.index) > 1):
            num_pieces = win_row_counts.loc[True]
            print(self.active_player[0] + " has " + str(num_pieces) + " pieces in this row")

            if (num_pieces > 3):
                seq = 0
                x = 0

                while x < len(win_row) and seq < 4 :
                    if (win_row[x] == True):
                        seq = seq + 1
                    else:
                        seq = 0
                    x = x + 1
                if (seq >= 4):
                    self.game_state = 1 #TODO: have this stop the game, maybe offer reset
                    self.win_print()
          
        #diag win check
        total_seq_1 = self.pos_diag_win_check(col, row, [], self.active_player[2])
        print("positive slope total " + str(total_seq_1))

        total_seq_2 = self.neg_diag_win_check(col, row, [], self.active_player[2])
        print("neg slope total " + str(total_seq_2))

        if (total_seq_1 >= 4 or total_seq_2 >= 4):
            self.game_state = self.active_player[2]
            self.win_print()       

    def win_print(self):
        s = self.active_player[0] + " wins!"
        plt.text(.75, 3, s, fontsize = 40, color = self.active_player[1])
        plt.pause(5)

    def pos_diag_win_check(self, col, row, checked, player):
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

    def prompt_player(self, s, c):
        plt.text(0, -0.25 , s, color = c)

    def next_player(self):
        self.turn = (self.turn + 1) % 2 #increments between 0 and 1 indicating player 1 and 2 respectively
        self.active_player = [self.player_names[self.turn], self.player_colors[self.turn], self.player_markers[self.turn]]
        self.prompt_player(self.active_player[0] + " your move!", self.active_player[1])
        print(self.active_player)

    def onclick(self, event):
            col = int(math.floor(event.xdata))
            self.check_df(col, -1)
            print(self.df)

    def __init__(self):
        #Set number of rows and columns for game board
        self.num_rows = 7 
        self.num_columns = 6

        #intitalize dataframe that will keep track of our game
        self.df = pd.DataFrame(np.zeros((self.num_rows,self.num_columns))).astype('int32')
        
        #create the matplot lib figure and populate it with tile
             
        fig, self.ax = plt.subplots()
        x_axis = np.arange(self.num_rows + 1) #+1 is needed for correct tiling
        y_axis = np.arange(self.num_columns + 1) #+1 is needed for correct tiling
        for x in range(len(x_axis)):
            line = np.zeros(len(y_axis)) + x
            plt.plot(line, np.arange(len(y_axis)), 'k')
        for y in range(len(y_axis)):
            line = np.zeros(len(x_axis)) + y
            plt.plot(np.arange(len(x_axis)), line, 'k')

        #links on click events from figure to onclick function
        cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
        #game state variable
        self.game_state = 0
        self.player_names = ['p1', 'p2']
        self.player_colors = ['r', 'b']
        self.player_markers = [1, -1]
        self.turn = 0
        self.active_player = [self.player_names[self.turn], self.player_colors[self.turn], self.player_markers[self.turn]] #provides, name, color and marker for active player
      
        self.prompt_player(self.active_player[0] + " your move!", self.active_player[1])

# class active_player():
#     def __init__(self):



g = Game()
while(g.game_state == 0):
    plt.pause(0.1)


