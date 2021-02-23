from board import Grid
from player import Player
from random import shuffle

def main():
    print("Welcome to Tic Tac Toe!")
    p1,p2 = Player(input("Player 1:")),Player(input("Player 2:"))
    p1.setSymbol('X')
    p2.setSymbol('O')
    
    new_board = Grid()
    new_board.fillSections()
    
    current_player,next_player = p1,p2 
    current_token, next_token = p1.getSymbol(),p2.getSymbol()
    move = None
    
    while True:
        print(new_board.drawGrid())
        
        move = int(input("What's your move? "))
        while not new_board.checkSpace(move):
            new_board.updateSection(move,current_token)
        
        if new_board.chickenWinner(current_token):
            print(new_board.drawGrid())
            print(f"{current_player} has won the game!")
            break
        elif new_board.itsFull():
            print(new_board.drawGrid())
            print("The Game is a tie!")
            break
        
        current_player,next_player = next_player, current_player
        current_token, next_token = next_token, current_token

main()