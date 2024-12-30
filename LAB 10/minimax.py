def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -10
    if winner == "O":
        return 10
    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def check_winner(board):
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] != " ":
            return board[i*3]
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    if board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ":
        return board[4]
    return None

def best_move(board):
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Example usage:
board = [" " for _ in range(9)]
board[0], board[4], board[8] = "X", "O", "X"  # Sample state
move = best_move(board)
print("Best move for O:", move)
