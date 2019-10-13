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
            if (S[0] != char_S):
                amt += 2
            if (S[leng_S - 1] != char_S):
                amt += 2
            for i in range(0, leng_S - 2, 2):
                fi = S[i]
                mi = S[i + 1]
                la = S[i + 2]
                if (fi == char_S and mi==char_S and la == char_S):
                    amt +=0
                elif(fi == char_S and mi== char_S and la != char_S):
                    amt += 0
                elif (fi == char_S and mi!= char_S and la == char_S):
                    amt += 2
                elif (fi != char_S and mi==char_S and la == char_S):
                    amt += 0
                elif (fi == char_S and mi!=char_S and la != char_S):
                    amt += 3
                elif (fi != char_S and mi==char_S and la != char_S):
                    amt += 1
                elif (fi != char_S and mi!=char_S and la == char_S):
                    amt += 3
                elif (fi != char_S and mi!=char_S and la != char_S):
                    amt += 4
    return amt

if __name__ == '__main__':
    input = 'bbbbbb'
    print(solution(input))
