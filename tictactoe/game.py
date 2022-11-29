import time
import math
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()        #using a single list to represent a 3x3 matrix
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        #this is to get the row
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: 
            print('| '+ ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        moves = []
        for (i,spot) in enumerate(self.board):
            if(spot == ' '):
                moves.append(i)

        return moves

    def empty_squares(self):
        return ' ' in self.board

    def empty_squares_num(self):
        return self.board.count(' ')  #you can also use return self.board.count(' ')

    def winner(self, square, letter):
        #this is to check whether there are 3 same letters in a row anywhere
        #first lets check row wise
        row_index = square//3
        row = self.board[row_index*3 : (row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        #if row didnt work, we check coloumn wise
        col_index = square % 3
        coloumn = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in coloumn]):
            return True

        #if row and col didnt work, we check diagonally
        if square % 2 == 0:
            diagonal1 =  [self.board[i] for i in [0,4,8]] #left diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 =  [self.board[i] for i in [2,4,6]] #right diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        return False



    def make_move(self, square, letter):
        if self.board[square]==' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'  #this is the starting letter

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter+ f" is added to the square {square}")
                game.print_board()
                print('') #just an empty line
        
        if game.current_winner:
            if print_game:
                print(letter + " wins!")
            return letter

        if letter == 'O': #to switch the players after every try
            letter = 'X'
        else:
            letter = 'O'
        time.sleep(.8)
        
        
    if print_game:
         print("It's a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)


