#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridGame' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY grid
#  2. INTEGER k
#  3. STRING_ARRAY rules
#

def gridGame(grid, k, rules):
    RULES = {'alive': 1, 'dead': 0}
    idx = [i for i, rule in enumerate(rules) if RULES[rule] == 1]
    for i in range(k):
        neighbour = counter(grid)
        grid = apply_rule(grid, neighbour, idx)
    return grid


def apply_rule(grid, neighbour, idx):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if neighbour[i][j] in idx:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid


def find_nn(x, y, m, n):
    return [(x2, y2) for x2 in range(x - 1, x + 2) for y2 in range(y - 1, y + 2) if (
                (-1 < x) and (x < m) and (-1 < y) and (y < n) and (0 <= x2 < m) and (0 <= y2 < n) and (
                    x != x2 or y != y2))]


def counter(grid):
    m = len(grid)
    n = len(grid[0])
    neighbour = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            nn = find_nn(i, j, m, n)
            for _n in nn:
                if grid[_n[0]][_n[1]] == 1:
                    neighbour[i][j] += 1
    return neighbour


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    rules_count = int(input().strip())

    rules = []

    for _ in range(rules_count):
        rules_item = input()
        rules.append(rules_item)

    result = gridGame(grid, k, rules)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

if __name__ == "__main__":
    k = 15
    arr = [12, 3, 4, 5, 5, 7, 8, 9, 7]
    print(targetsum_set(arr, k))
    print(targetsum_sort(arr, k))