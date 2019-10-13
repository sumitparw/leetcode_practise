import string
def lengthOfLongestSubstring(s):
    leng = len(s)
    if (s == 0):
        return 0
    elif (s == 1):
        return 1
    #temp = list()
    alphaDict = dict.fromkeys(s.ascii_lowercase,0)
    print(alphaDict)
    max_len = 0
    k = 0
    for i in range(0, len(s), 1):
        temp = list()
        if(i>0):
            i = k
        temp.append(s[i])
        for j in range(i + 1, len(s), 1):
            if (s[j] not in temp):
                temp.append(s[j])
            else:
                k = j
                break
        if (len(temp) > max_len):
            max_len = len(temp)
    return (max_len)

a = lengthOfLongestSubstring("pwwkew")
print(a)