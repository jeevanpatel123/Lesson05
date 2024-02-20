import random

def get_player_move():
    player_move = input('Choose ROCK, PAPER, or SCISSORS:\n\n')
    if player_move not in ['ROCK', 'PAPER', 'SCISSORS']:
        print("PLAYER MOVE INVALID")
        player_move = input('Choose ROCK, PAPER, or SCISSORS:\n\n')
    return player_move

def get_computer_move():
    return random.choice(['ROCK', 'PAPER', 'SCISSORS'])

def get_winner(player_move, computer_move):
    if player_move == 'ROCK' and computer_move == 'SCISSORS':
        return "YOU WIN!"
    elif player_move == 'PAPER' and computer_move == 'ROCK': 
        return "YOU WIN!"
    elif player_move == 'SCISSORS' and computer_move == 'PAPER':
        return "YOU WIN!"
    elif player_move == computer_move:
        return "TIE GAME!"
    else:
        return "COMPUTER WINS!"

def main():
    print("WELCOME TO ROCK PAPER SCISSORS!!")
    
    while True:
        player_move = get_player_move()
        computer_move = get_computer_move()
        
        print("YOU CHOSE:", player_move)
        print("COMPUTER CHOSE", computer_move)
        
        print(get_winner(player_move, computer_move))
        
        repeat_game = input('WOULD YOU LIKE TO PLAY AGAIN? YES/NO:\n')
        if repeat_game != 'YES':
            break

if __name__ == "__main__":
    main()
        
