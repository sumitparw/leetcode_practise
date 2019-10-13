import collections
def first_unique(inp):
    s = collections.Counter(inp)
    for idx, ch in enumerate(s):
        if s[ch] == 1:
            return (idx)
    return -1
inp ='loveleetcode'
print(first_unique(inp))

