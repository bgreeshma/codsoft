import random

def play_round():
    # Choices for the game
    choices = ['rock', 'paper', 'scissors']
    
    # Taking user input
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # Ensure valid input from user
    while user_choice not in choices:
        user_choice = input("Invalid choice! Please enter rock, paper, or scissors: ").lower()

    # Randomly generating computer's choice
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    while True:
        play_round()
        
        # Ask if the user wants to play another round
        play_again = input("Do you want to play again? (yes/no): ").lower()
        
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
play_game()