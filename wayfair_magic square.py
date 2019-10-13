# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import numpy as np
def isMagicSquare(mat):
    # calculate the sum of
    # the prime diagonal
    s = 0
    N = len(mat)

    for i in range(0, N):
        s = s + mat[i][i]

        # the secondary diagonal
    s2 = 0
    for i in range(0, N):
        s2 = s2 + mat[i][N - i - 1]

    if (s != s2):
        return False

    # For sums of Rows
    for i in range(0, N):
        rowSum = 0;
        for j in range(0, N):
            rowSum += mat[i][j]

            # check if every row sum is
        # equal to prime diagonal sum
        if (rowSum != s):
            return False

    # For sums of Columns
    for i in range(0, N):
        colSum = 0
        for j in range(0, N):
            colSum += mat[j][i]

            # check if every column sum is
        # equal to prime diagonal sum
        if (s != colSum):
            return False

    return True


def solution(A):
    oup = False
    # write your code in Python 3.6
    num_rows = len(A)  # 3 rows in your example
    num_cols = len(A[0])
    lis = [1, -1]
    k = 2
    max_s = 0
    while (k < 20):
        for i in range(num_rows - k+1):
            for j in range(num_cols - k+1):
                oup = isMagicSquare(A[i:i + k, j:j + k])
                if oup == True and k>max_s:
                    max_s = k
        k += 1
    return max_s
if __name__ == '__main__':
    input = np.array([[2, 2, 1, 1], [2, 2, 2, 2], [1, 2, 2, 2]])
    # print(input)
    # print(input[0:2, 0:2])
    print(solution(input))