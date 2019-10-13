board =[["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
print(board)
numrows = len(board)
if (numrows != 0):
    numcols = len(board[0])
    for i in range(0,numrows,1):
        for j in range(0,numcols,1):
            if(i == 0):
                continue
            elif(i == numrows-1):
                continue
            elif(j == 0):
                continue
            elif(j == numcols-1):
                continue
            elif(i==1):
                if(board[i-1][j]!="O"):
                    board[i][j] = "X"
                else:
                    continue
            elif (i == numrows-2):
                if (board[i +1][j] != "O"):
                    board[i][j] = "X"
                else:
                    continue
            elif (j == 1):
                if (board[i][j-1] != "O"):
                    board[i][j] = "X"
                else:
                    continue
            elif (j == numcols - 2):
                if (board[i][j+1] != "O"):
                    board[i][j] = "X"
                else:
                    continue
            elif(board[i][j]=="O"):
                board[i][j] = "X"
            else:
                continue
print(board)