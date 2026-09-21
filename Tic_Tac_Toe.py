import random as r

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

while True:
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

    choice = int(input("Choose a spot (1-9): ")) 
    board[choice] = "X"

    
    if (board[0] == board[1] == board[2] == "X" or
        board[3] == board[4] == board[5] == "X" or
        board[6] == board[7] == board[8] == "X" or
        board[0] == board[3] == board[6] == "X" or
        board[1] == board[4] == board[7] == "X" or
        board[2] == board[5] == board[8] == "X" or
        board[0] == board[4] == board[8] == "X" or
        board[2] == board[4] == board[6] == "X"):
        print("You win!")
        break

    if " " not in board:
        print("It's a tie!")
        break

    
    empty_spots = []
    for i in range(9):
        if board[i] == " ":
            empty_spots.append(i)

    computer_choice = r.choice(empty_spots)
    board[computer_choice] = "O"
    print(f"Computer chose spot {computer_choice + 1}")

    
    if (board[0] == board[1] == board[2] == "O" or
        board[3] == board[4] == board[5] == "O" or
        board[6] == board[7] == board[8] == "O" or
        board[0] == board[3] == board[6] == "O" or
        board[1] == board[4] == board[7] == "O" or
        board[2] == board[5] == board[8] == "O" or
        board[0] == board[4] == board[8] == "O" or
        board[2] == board[4] == board[6] == "O"):
        print("Computer wins!")
        break
