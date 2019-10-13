import heapq
def klargest(nums,k):
    return (sorted(nums)[len(nums) - k])
def optimized(arr,k):
    print(heapq.heapify(arr))
    print(arr)
    #heapq.heappushpop(arr, 45)
    for i in range(7):
      print(heapq.heappop(arr))
    print(arr)

if __name__ == "__main__":
    arr = [2,5,-51,98,46,1,24,23,46]
    k = 3
    print(klargest(arr,k))
    optimized(arr, k)