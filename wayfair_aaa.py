# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import numpy as np
def solution(S):
    leng_S = len(S)
    char_S = 'a'
    amt = 0
    new_string = ''
    if 'aaa' in S:
        amt = -1
    else:
        if (leng_S == 1):
            if (S[0] == char_S):
                amt = 1
            else:
                amt = 4
        elif (leng_S == 2):
            if ((S[0] == char_S and S[1] != char_S) or (S[0] != char_S and S[1] == char_S)):
                amt = 3
        elif (leng_S > 2):
            amt = (leng_S+1)*2
            count_a = 0
            count_aa = 0
            for i in range(leng_S):
                if S[i] == 'a':
                    count_a += 1
            for i in range(0,leng_S-1,1):
                if S[i] + S[i+1] == 'aa':
                    count_aa += 1
            amt = amt - count_a*(3)
            amt = amt - count_aa * (6)
    return amt

if __name__ == '__main__':
    input = 'babababa'
    print(solution(input))
