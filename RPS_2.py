import random

def get_player_move():
    player_move = input('Please Enter ROCK, PAPER, or SCISSORS:\n\n')
    if player_move not in ['ROCK', 'PAPER', 'SCISSORS']:
        print("Player Choice Invalid")
        player_move = input('Please Enter ROCK, PAPER, or SCISSORS')
    return player_move

def get_computer_move():
    return random.choice(['ROCK', 'PAPER', 'SCISSORS'])

def winner(player_move, computer_move):
    if player_move == 'ROCK' and computer_move == 'SCISSORS':
        return "YOU WIN!"
    elif player_move == 'PAPER' and computer_move == 'ROCK':
        return "YOU WIN!"
    elif player_move == 'SCISSORS' and computer_move == 'PAPER':
        return "YOU WIN!"
    elif player_move == computer_move:
        return "TIE GAME!"
    else:
        return ("COMPUTER WINS!")
    

def main():
    print("WELCOME TO ROCK PAPER SCISSORS!!")
    
    while True:
        player_move = get_player_move()
        computer_move = get_computer_move()
        
        print("You Chose:", player_move)
        print("Computer Chose", computer_move)
        
        print(winner(player_move, computer_move))
        
        repeat_game = input("Play Again? Yes/No:\n\n")
        if repeat_game != 'Yes':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
            
        
    

