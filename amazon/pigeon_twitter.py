def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    print(K)
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


def maximumTotalWeight(weights, tasks, p):
        p = p
        n = len(weights)
        tasks = [2 * i for i in tasks]
        return knapSack(p, tasks, weights, n)

if __name__ =="__main__":
    p = 9
    weights = [3, 2, 2]
    tasks = [3, 2, 2]
    print(maximumTotalWeight(weights, tasks, p))