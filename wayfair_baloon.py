# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    dict_need = [1, 1, 2, 2, 1]
    dict_S = {}
    dict_S['B'] = 0
    dict_S['A'] = 0
    dict_S['L'] = 0
    dict_S['O'] = 0
    dict_S['N'] = 0
    for i in range(len(S)):
        if S[i] == 'B':
            dict_S['B'] += 1
        elif S[i] == 'A':
            dict_S['A'] += 1
        elif S[i] == 'L':
            dict_S['L'] += 1
        elif S[i] == 'O':
            dict_S['O'] += 1
        elif S[i] == 'N':
            dict_S['N'] += 1
        else:
            continue

    cnt = 0
    flag = True
    print(dict_S)
    while (flag == True):
        j = 0
        for key in dict_S:
            dict_S[key] = dict_S[key] - dict_need[j]
            #print(dict_S[key])
            if (dict_S[key] < 0):
                flag = False
                break
            j += 1
        if (flag == True):
            cnt += 1
    return cnt


if __name__ == '__main__':
    input = 'BAOOLLNNOLOLGBAX'
    print(solution(input))