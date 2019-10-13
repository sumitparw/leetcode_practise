from itertools import permutations


def solution(N):
    # write your code in Python 3.6

    # Get all permutations of [1, 2, 3]

    str_N = str(N)
    print(list(str_N))
    max_ = N
    perm = permutations(list(str_N))
    #print(perm)
    for i in list(perm):
        xx  = ''.join(i)
        if(int(xx)>max_):
            max_= int(xx)
    return(max_)


if __name__ == '__main__':
    input = 58488314
    print(solution(input))
