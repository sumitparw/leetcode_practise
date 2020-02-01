# Python3 program to count Triplets such
# that at least one of the numbers can be
# written as sum of the other two
import math as mt


# Functoin to count the number of ways
# to choose the triples
def countWays(arr, n):
    # compute the max value in the array
    # and create frequency array of size
    # max_val + 1.
    # We can also use HashMap to store
    # frequencies. We have used an array
    # to keep remaining code simple.
    max_val = max(arr)
    # for i in range(n):
    #     max_val = max(max_val, arr[i])
    # print(max_val)
    freq = [0 for i in range(max_val+1)]
    for i in range(n):
        freq[arr[i]] += 1
    ans = 0  # stores the number of ways

    # Case 1: 0, 0, 0
    ans += (freq[0] * (freq[0] - 1) *
            (freq[0] - 2) // 6)

    # Case 2: 0, x, x
    for i in range(1, max_val + 1):
        ans += (freq[0] * freq[i] *
                (freq[i] - 1) // 2)

        # Case 3: x, x, 2*x
    for i in range(1, (max_val + 1) // 2):
        ans += (freq[i] *
                (freq[i] - 1) // 2 * freq[2 * i])

        # Case 4: x, y, x + y
    # iterate through all pairs (x, y)
    for i in range(1, max_val + 1):
        for j in range(i + 1, max_val - i + 1):
            ans += freq[i] * freq[j] * freq[i + j]

    return ans


# Driver code
arr = [1, 2, 3, 4, 5]
n = len(arr)
print(countWays(arr, n))
