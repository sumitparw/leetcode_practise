
def lengthOfLongestSubstring(s):
    leng = len(s)
    if (s == 0):
        return 0
    elif (s == 1):
        return 1
    #temp = list()
    k = 0
    max_len = 0
    for i in range(0, len(s), 1):
        temp = list()
        temp.append(s[i])
        for j in range(i+1, len(s), 1):
            if (s[j] not in temp):
                temp.append(s[j])
            else:
                break
        if (len(temp) > max_len):
            max_len = len(temp)
    return (max_len)


a = lengthOfLongestSubstring("pwwkew")
print(a)