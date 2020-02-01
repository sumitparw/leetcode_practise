def subArraySum(arr, n, Sum):
    # create an empty map
    Map = {}
    curr_sum =0
    for i in range(n):
        print(Map)
        curr_sum += arr[i]
        if curr_sum == Sum:
            print("sum is from index 0 to", i)
        if curr_sum-Sum in Map:
            print("sum is from index", Map[curr_sum-Sum]+1, "to ", i)
        Map[curr_sum] = i


if __name__ == "__main__":
    arr = [10, 2, 2, 20, 10]
    n = len(arr)
    Sum = 30

    subArraySum(arr, n, Sum)