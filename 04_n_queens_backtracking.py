def is_safe(board,row,col):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)==row-i:
            return False
    return True


def print_board(board,n):
    for i in range(n):
        line=["Q"if board[i]==j else "."for j in range(n)]
        print(" ".join(line))

def solve(board,row,n):
    if row==n:
        return True
    for col in range(n):
        if is_safe(board,row,col):
            board[row]=col
            if solve(board,row+1,n):
                return True
            board[row]=-1
    return False

def n_queen(n):
    board=[-1]*n
    if solve(board,0,n):
        print_board(board,n)
    else:
        print("not solvable")
n_queen(4)
