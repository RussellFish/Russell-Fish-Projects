# Russell Fish
class Board(object):
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.board = self.createBoard()
        
    def createOneRow(self): #Helper Function for createBoard that creates a single row
        row = []
        for x in range(self.width):
            row += ['']
        return row

    def createBoard(self):
        """Creates the Connect Four Board"""
        X = []
        for r in range(self.height):
            X += [self.createOneRow()]
        return X   
    
    def allowsMove(self, col):
        """Returns False if col if full and True if col is not"""
        try:
            int(col)
        except:
            return False
        col = int(col)
        if col in list(range(self.width)):
            if self.board[0][col] == '':
                return True
            else:
                return False
        else:
            return False
        
    def addMove(self, col, ox):
        """Drops and xo into col"""
        if self.allowsMove(col) == True:
            I = -1
            for row in self.board:
                if row[col] == '':
                    I += 1
                else:
                    break
            self.board[I][col] = ox
                                     
    def setBoard(self, moveString):
        """ takes in a string of columns and places
         alternating checkers in those columns,
         starting with 'X'"""
        nextCh = 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
                
    def delMove(self, col):
        """Deletes the top moved from col"""
        if self.board[self.height-1][col] != '':
            p = 0
            x=[]
            while p < self.height:
                if self.board[p][col] == '':
                    p += 1
                else:
                    self.board[p][col] = ''
                    
    def winsFor(self, xo):
        """Checks if xo has won"""
        #Checks for Horizontal Win
        for row in range(self.height):
            Hc = 0
            for col in range(self.width):
                if self.board[row][col] == xo:
                    Hc += 1
                    if Hc >= 4:
                        return True
                else:
                    Hc = 0
                
        #Checks for Vertical Win
        for col in range(self.width):
            Vc = 0
            for row in range(self.height):
                if self.board[row][col] == xo:
                    Vc += 1
                    if Vc >= 4:
                        return True
                else:
                    Vc = 0
                    
        #Checks for Diagonal Win 1/4
        for row in range(self.height):
            x = 0 
            y = row
            Dc = 0 
            while x < self.width and  y > -1:
                if self.board[y][x] == xo:
                    Dc += 1
                    if Dc >= 4:
                        return True
                    else:
                        x +=1
                        y -= 1
                else:
                    Dc = 0
                    x += 1
                    y -= 1
        
        #Checks for Diagonal Win 2/4
        for col in range(self.width):
            x = col
            y = self.height - 1
            Dc = 0
            while x < self.width and y > -1:
                if self.board[y][x] == xo:
                    Dc += 1
                    if Dc >= 4:
                        return True
                    else:
                        x -= 1
                        y -= 1
                else:
                    Dc = 0
                    x -= 1
                    y -= 1
                    
        #Checks for Diagonal Win 3/4
        for col in range(self.width):
            x = col
            y = self.height -1
            Dc = 0
            while x < self.width and y > -1:
                if self.board[y][x] == xo:
                    Dc += 1
                    if Dc >= 4:
                        return True
                    else:
                        x+= 1
                        y -= 1
                else:
                    Dc = 0
                    x += 1
                    y -= 1
                    
        #Checks for Diagonal Win 4/4
        for row in range(self.height):
            x = 0
            y = row
            Dc = 0
            while x < self.width and y > -1:
                if self.board[y][x] == xo:
                    Dc += 1
                    if Dc >= 4:
                        return  True
                    else:
                        x += 1
                        y -= 1
                else:
                    Dc = 0 
                    x += 1
                    y -= 1
        return False
        #return False
                        
    def __str__(self):
        """Returns the input sized Connect Four Board"""
        Y = ''
        
        for row in range(self.height):
            if row > 0:
                Y += '\n'
            for col in range(self.width):
                if self.board[row][col] == '':
                    Y += '| '
                else:
                    Y += ('|' + self.board[row][col])
            Y += '|'
        
        Y += ('\n' + '-' * 2 * self.width + '\n')
        
        for i in range(self.width):
            Y += (' ' + str(i))
            
        return Y
    
    def hostGame(self):
        """Loops the program so a game of Connect Four is played on the given board until either player has won"""
        print("Welcome to Connect Four!\n")
        while True:
            print(self, '\n')
            X = input("X player enter your column choice.\n")
            while True:
            #Player One's Turn
                if self.allowsMove(X) == True:
                    print("X's choice: " + X + "\n")
                    self.addMove(int(X), "X")
                    print(self, '\n')
                    break
                else:
                    X = input(X + " is not a valid move." + " X player enter a valid column choice.\n")
                    
            if self.winsFor("X") == True:
                print("X wins -- TAKE THAT O!")
                break
            
            #Player Two's Turn
            O = input("O player enter your column choice.\n")
            while True:
                if self.allowsMove(O) == True:
                    print("O's choice: " + O)
                    self.addMove(int(O), "O")
                    print(self, "\n")
                    break
                else:
                    O = input(O + " is not a valid move." + " O player enter a valid column choice.\n")
                    
            
            if self.winsFor("O") == True:
                print("O wins -- OOF BETTER LUCK NEXT TIME X!")
                break
if __name__ == "__main__":

    b = Board()
    b.hostGame()

