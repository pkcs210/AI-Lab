def print_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def check_winner(board, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def main():
    board = [' ']*9
    current_player = 'X'
    for _ in range(9):
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) -1
            if board[move] == ' ':
                board[move] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    return
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Enter a number from 1 to 9.")
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()
