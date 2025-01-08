import random

# Function to determine the winner of a round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

# Main game function
def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # User input: ask for rock, paper, or scissors
        user_choice = input("Choose 'rock', 'paper', or 'scissors': ").lower()
        
        # Validate input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Computer makes a random choice
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        
        # Update scores and display result
        if result == "win":
            user_score += 1
            print("You win this round!")
        elif result == "lose":
            computer_score += 1
            print("You lose this round.")
        else:
            print("It's a tie!")
        
        # Display the current scores
        print(f"Scores -> You: {user_score} | Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

# Run the game
play_game()
