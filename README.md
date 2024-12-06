# Instructions

This is a simple **Rock, Paper, Scissors** game where you can play against the computer in a command-line interface.

## How to Play

1. The game will prompt you to choose one of the following options:
   - **1**: Rock
   - **2**: Paper
   - **3**: Scissors

2. The computer will then randomly pick one of the three options as well.

3. The game will compare your choice to the computer's choice and display the result:
   - **You win!**: If your choice beats the computer's choice.
   - **You lose!**: If the computer's choice beats yours.
   - **It's a tie!**: If both you and the computer choose the same option.

4. The game continues until you choose to quit by entering **0**.

## Features

- Play against a randomly selected computer choice.
- Option to quit the game anytime by entering **0**.
- User input validation to ensure only valid choices are accepted.
- Displays the outcome of each round and keeps running until the user decides to quit.

## Installation

To run the game, simply clone or download the repository and run the Python script.

```bash
git clone https://github.com/yourusername/rock-paper-scissors.git
cd rock-paper-scissors
python3 rock_paper_scissors.py
```

### Requirements
- Python 3.x


### How It Works
1. The program uses a dictionary to map user choices (1, 2, 3) to "rock", "paper", and "scissors".
2. It takes user input and validates it.
3. The computer randomly selects one of the three options.
4. The result of the game is determined by comparing the user’s and the computer's choices.
5. The game continues until the user inputs 0 to quit.

## Example Output

```
Choose an option:
1: Rock
2: Paper
3: Scissors
Enter '0' to quit

Your choice (1/2/3): 1
Computer chose paper
You lose!
```
