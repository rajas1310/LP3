import random

N = int(input("Enter the number of queens to be placed = "))

board = [[0 for i in range(N)] for _ in range(N)]

def isAttacked(i,j):
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

        for l in range(N):
            if (k+l == i+j or k-l==i-j) and board[k][l] == 1:
                return True
    return False

def nQueens(n):
    if n == 0:
        return True

    for i in range(N):
        for j in range(N):
            if (isAttacked(i,j)==False and board[i][j] != 1):
                board[i][j] = 1
                if nQueens(n-1) == True:
                    return True
                board[i][j] = 0

    return False

rand_row = 2 #random.randrange(0,N)
rand_col = 0 #random.randrange(0,N)
print("First Q placed at: (",rand_row,",",rand_col,")")
board[rand_row][rand_col] = 1

status = nQueens(N-1) # N-1 because 1 Queen is already placed

if status:
    for i in board:
        print(i)

else:
    print("Solution not possible...")
