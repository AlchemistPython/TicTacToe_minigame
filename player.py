class Player:
    def __init__(self,name_player):
        self.name = name_player
    
    def setSymbol(self,symbol):
        self.symbol = symbol
    
    def getSymbol(self):
        return self.symbol
    
    def __str__(self):
        return self.name
