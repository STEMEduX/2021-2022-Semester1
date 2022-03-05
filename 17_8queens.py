#8queens.py
#Backtracking the solution of the problem depends on the previous steps taken. We take a step and then #analyze it that whether it will give the correct answer or not? and if not, then we move back and #change the previous step.

# Define functions:
def attack(i, j):
    #checking vertically and horizontally
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonally
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False
  
def N_queens(n):
    print ("Checking on N_queens ", n)
  
    if n==0:
        return True
    for i in range(0,N): # exmine the columns
        for j in range(0,N): # exmine the rows
            # If no queen in vertial line or horizontal 
            # line or in diagonal line and in board 
            # position (i,j), then put a queen in (i,j)
            if (not(attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                # Now do backtracking via recursive Call
                if N_queens(n-1)==True: 
                    print ("Checking on N_queens ", n, " is true")
                    # this row j at column i seems to be no attack,
                    # exit the recursive function called for (n-1)
                    # and move back to N_queens(n) and N_queens(n)
                    # will move to next(i) column
                    return True
                # If backtracking is False, then
                # we can't put a queen in (i,j), and
                # we continue to examine next position in this loop 
                # in N x N board
                board[i][j] = 0
    return False

# Taking number of queens as input from user
print ("Enter the number of queens")
N = int(input())
# here we create a chessboard
# NxN matrix with all elements set to 0
board = [[0]*N for _ in range(N)]

N_queens(N)

# Print results
for i in board:
    print (i)
