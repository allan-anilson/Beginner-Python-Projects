import random
import math

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        #computer chooses random position from the board for the next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Please select an integer from (0-8)')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid Square! Try again!")

        return val

class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #here we implement the minmax algorithm to choose a square
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, currentstate, player):
        max_player = self.letter #yourself!
        other_player = 'O' if player == 'X' else 'X'

        #we are gonna use recursion inorder to implement the algorithm tree
        #this is our base case
        #check whether the previous move was a winner
        if currentstate.current_winner == other_player:
            return{'position': None, 'score':  1*(currentstate.empty_squares_num()+1) if other_player == max_player 
            else -1*(currentstate.empty_squares_num()+1) }

        elif not currentstate.empty_squares(): #no empty squares
            return {'position':None, 'score':0}

        if player == max_player:
            best = {'position':None, 'score':-math.inf}#each score should maximize(be larger)
        else:
            best = {'position':None, 'score': math.inf}#each score should minimize(be smaller)

        for possible_move in currentstate.available_moves():
            #step1:make a move, try that spot
            currentstate.make_move(possible_move,player)
            #step2:recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(currentstate, other_player)
            #step3:undo the move
            currentstate.board[possible_move] = ' '
            currentstate.current_winner = None
            sim_score['position'] = possible_move
            #step4:update the dictionaries if neccessary
            if player == max_player: #here we maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:                 #here we minimize the other player
                if sim_score['score'] < best['score']:
                   best = sim_score

        return best




    