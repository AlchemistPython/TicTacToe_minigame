class Grid:
    def __init__(self):
        self.board = {}
        self.numerical_section = [n for n in range(1,10)]
    
    def fillSections(self):
        self.board= dict((x,str(x)) for x in self.numerical_section)
        return self.board
    
    def drawGrid(self):
        return """
     {} | {} | {}
     __|___|__
     {} | {} | {}
     __|___|__
     {} | {} | {}
    """.format(self.board[1],self.board[2],self.board[3],self.board[4],self.board[5],self.board[6],self.board[7],self.board[8],self.board[9])
    
    def updateSection(self,value,mark):
        self.board[value] = mark
        
    # verifica que el numero que ingreso sea de los que estan en la seccion    
    def checkSpace(self,number):
        tokens = ['X','O']
        return number in self.numerical_section and self.board[number] in tokens

    def itsFull(self):
        
        tokens = ['X','O']
        full = True
        
        for value in self.board.values():
            if not value in tokens:
                full = False
        return full
    
    def chickenWinner(self,mark):
        # acrossTop,acrossMiddle,acrossBot,downLeft,downMiddle,downRight,diagonalRight,diagonalLeft
        pattern = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        counter = 0
        won = False
        
        for rows in pattern:
            for cols in rows:
                if self.board[cols] == mark:
                    counter += 1
            if counter == 3:
                won = True
                break    
            else:
                counter = 0
        return won                 
