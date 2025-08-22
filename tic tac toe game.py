# Tic Tac Toe Game

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Rows, Columns, Diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2-i] == player for i in range(3)): return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    turns = 0

    while turns < 9:
        print_board(board)
        p = players[turns % 2]
        try:
            r, c = map(int, input(f"Player {p} enter row col (0-2): ").split())
        except:
            print("Invalid input! Use two numbers between 0-2.")
            continue

        if r not in range(3) or c not in range(3) or board[r][c] != " ":
            print("Invalid move! Try again.")
            continue

        board[r][c] = p
        if check_winner(board, p):
            print_board(board)
            print(f"Player {p} wins!")
            return
        turns += 1

    print_board(board)
    print("It's a Draw!")

if __name__ == "__main__":
    tic_tac_toe()
