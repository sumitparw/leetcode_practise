import heapq
import collections

def frequencySort(s):
    counter = collections.Counter(s)
    output = "".join(char * freq for char, freq in counter.most_common())
    return output

input = "tree"
print(frequencySort(input))
