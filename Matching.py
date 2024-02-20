import random

print("Welcome to the Matching Game!!")
print()
def get_player_choice():
    player_choice = input('Enter Apple, Banana, or Cherry:\n\n') 
    if player_choice not in ['Apple', 'Banana', 'Cherry']:
        print("player choice is invalid")
        player_choice = input('Enter Apple, Banana, or Cherry:\n\n')
    return player_choice

def get_computer_choice():
    return random.choice(['Apple', 'Banana', 'Cherry'])

def game_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Matched!"
    elif player_choice != computer_choice:
        return "Not Matched"  

def main():  
    while True: 
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
    
        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)
        
        print(game_winner(player_choice, computer_choice))
        
        repeat_game = input('Play again? (yes/no):\n').lower()
        if repeat_game != 'yes':
            print("Thanks for playing!")
            break    

if __name__ == "__main__":
    main()