import random
def play():
    player = input("Choose 'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])
    if player == computer:
        return 'Tie'
    if is_win(player, computer):
        return 'You Win!'
    return 'You Lost!'

def is_win(player,computer):
    #r>s, p>r, s>p
    if(player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True

print(play())