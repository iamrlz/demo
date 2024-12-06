import random

# Mapping numbers to choices
options = {1: "rock", 2: "paper", 3: "scissors"}

def display_score(user_score, computer_score):
    print(f"\nCurrent Score - You: {user_score} | Computer: {computer_score}")

def display_history(history):
    print("\nGame History:")
    for round_num, (user_move, computer_move, result) in enumerate(history, 1):
        print(f"Round {round_num}: You chose {user_move}, Computer chose {computer_move} - {result}")

# Initialize scores and history
user_score = 0
computer_score = 0
history = []

# Get number of rounds for the game
while True:
    try:
        rounds = int(input("Enter the number of rounds you want to play (or '0' to quit): "))
        if rounds == 0:
            print("Thanks for playing!")
            break
        elif rounds < 1:
            print("Please enter a positive number.")
        else:
            print(f"Great! Let's play Best of {rounds} rounds.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

current_round = 1
while current_round <= rounds:
    # Display options to the user
    print("\nChoose an option:")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    print("Enter '0' to quit")

    # Get user choice
    try:
        user_choice = int(input("Your choice (1/2/3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Handle quitting the game
    if user_choice == 0:
        print("Thanks for playing!")
        display_history(history)
        break
    
    # Validate user choice
    if user_choice not in options:
        print("Invalid choice. Please choose 1, 2, or 3.")
        continue

    # Random choice for computer
    computer_choice = random.randint(1, 3)
    print(f"\nYou chose {options[user_choice]}")
    print(f"Computer chose {options[computer_choice]}")

    # Determine the outcome
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    # Record round result
    history.append((options[user_choice], options[computer_choice], result))
    print(result)
    display_score(user_score, computer_score)
    
    # Check if we reached the end of Best of N rounds
    if user_score > rounds // 2 or computer_score > rounds // 2:
        break

    current_round += 1

# Display final results and history
print("\nFinal Results:")
display_score(user_score, computer_score)
display_history(history)

if user_score > computer_score:
    print("Congratulations! You won the game!")
elif user_score < computer_score:
    print("Sorry, the computer won the game. Better luck next time!")
else:
    print("It's a tie game overall!")

print("Thanks for playing!")
