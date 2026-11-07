# Creating a small tic-tac-toe game
# We are playing as X and the computer plays as O

# random is a python tool used here to add random positions where the computer will do its move 
import random

# The board is a list of 9 squares. At first each square shows its number so the player can see which number to type to choose a square.
# It will count list positions from 0, so square 1 is grid[0], square 2 is grid[1] and so on
grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Creating a function that prints the current board in a 3x3 grid
def ShowBoard():
    print(grid[0] + " | " + grid[1] + " | " + grid[2])
    print("--+---+--")
    print(grid[3] + " | " + grid[4] + " | " + grid[5])
    print("--+---+--")
    print(grid[6] + " | " + grid[7] + " | " + grid[8])


# This function checks whether any player has made a row of three matching marks which marks him the winner
# It returns the mark of the winner (X or O)
def CheckWinner():
    # Checking three horizontal rows whether they contain contiguous squares
    if grid[0] == grid[1] == grid[2]:
        return grid[0]
    if grid[3] == grid[4] == grid[5]:
        return grid[3]
    if grid[6] == grid[7] == grid[8]:
        return grid[6]

    # Checking three vertical columns whether they contain contiguous rows
    if grid[0] == grid[3] == grid[6]:
        return grid[0]
    if grid[1] == grid[4] == grid[7]:
        return grid[1]
    if grid[2] == grid[5] == grid[8]:
        return grid[2]

    # Checking the diagonal and anti diagonal line if they contain contigious squares
    if grid[0] == grid[4] == grid[8]:
        return grid[0]
    if grid[2] == grid[4] == grid[6]:
        return grid[2]

    # If none of the rows, columns, or diagonals matched, there is no winner yet
    return ""

# Starting with the main interface and prompting the user to give the input for the first move
print("Welcome! Choose a square by typing its number.")
ShowBoard()

# There are 9 squares, so the game can have at most 9 moves
for turn in range(9):
    # The remainder (%) is 0 on turns 0, 2, 4, 6, and 8 which makes the human player go first, then the computer
    if turn % 2 == 0:
        move = int(input("Your move (1-9): "))

        # Here we are prompting user to give input until he inputs a empty square which isn't used
        # move - 1 changes the player's number (1-9) into a list position (0-8)
        while move < 1 or move > 9 or grid[move - 1] == "X" or grid[move - 1] == "O":
            print("That square is not available. Try again.")
            move = int(input("Your move (1-9): "))

        # What the user inputs, insert it into the board
        grid[move - 1] = "X"
    else:
        # Here we are making a list of empty squares such that we design the computer's move on these available squares only
        empty_squares = []
        for i in range(9):
            if grid[i] != "X" and grid[i] != "O":
                # Save this list position because the computer can choose it.
                empty_squares.append(i)

        # random.choice picks one of those available positions at random beacuse import.random was included in the code
        computer_move = random.choice(empty_squares)
        grid[computer_move] = "O"

        # Adding 1 such that the list position changes into square position in real
        print("The computer chose square", computer_move + 1)

    # Showing the board after each player has made a move
    ShowBoard()

    # Checking board after each move if the game ends or not
    winner = CheckWinner()
    if winner == "X":
        print("You win!")
        break  # Stopping the loop because you won
    elif winner == "O":
        print("The computer wins!")
        break  # Stopping the loop because computer won
    # else runs when the loop finishes without a break which means all 9 moves have been made and it is a draw since no one won
    print("It's a draw!")
