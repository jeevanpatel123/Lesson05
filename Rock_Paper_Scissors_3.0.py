import random

def this_player_move():
    player_move = input('Enter Rock, Paper, or Scissors:\n')
    if player_move not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid Response")
        player_move = input('Enter Rock, Paper, or Scissors:\n')
    return player_move

def this_computer_move():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def this_game_winner(player_move, computer_move):
    if player_move == computer_move:
        return ("Tie Game!")
    elif player_move == 'Rock' and computer_move == 'Scissors':
        return ("You Win!")
    elif player_move == 'Paper' and computer_move == 'Rock':
        return ("You Win!")
    elif player_move == 'Scissors' and computer_move == 'Paper':
        return ("You Win!")
    else:
        return ("Computer Wins!")
        
def main_function():
    print("WELCOME TO ROCK PAPER SCISSORS!!\n\n")
# Need this to make the loop.
    while True:
        player_move = this_player_move()
        computer_move = this_computer_move()
        
        print("You chose:", player_move)
        print("Computer chose:", computer_move)
        
        winner = this_game_winner(player_move, computer_move)
        print(winner)
        
        repeat_game = input('Play again? (yes or no):\n')
        if repeat_game != 'yes':
            break
        
# Need this to make the loop.
if __name__ == "__main__":
    main_function()