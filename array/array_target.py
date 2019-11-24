# Python program to find if there are
# two elements wtih given sum

# function to check for the given sum
# in the array
def printPairs(arr, arr_size, sum):
    # Create an empty hash set
    s = set()

    for i in range(0, arr_size):
        temp = sum - arr[i]
        print(temp)
        if (temp in s):
            print("Pair with given sum " + str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")")
        s.add(arr[i])
    print(s)

    # driver program to check the above function


A = [1, 3,4,4,5]
n = 8
printPairs(A, len(A), n)