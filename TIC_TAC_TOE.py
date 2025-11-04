def print_board(board):
    
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
  
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
   
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")
        try:
            row = int(input("Enter row (0,1,2): "))
            col = int(input("Enter col (0,1,2): "))
        except ValueError:
            print("Invalid input! Enter numbers 0, 1, or 2.")
            continue

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid position! Choose between 0–2.")
            continue
        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

       
        board[row][col] = current_player
        print_board(board)

       
        if check_winner(board, current_player):
            print(f"Player {current_player} wins! 🎉")
            break
        if is_full(board):
            print("It's a draw!")
            break

       
        current_player = "O" if current_player == "X" else "X"



tic_tac_toe()
