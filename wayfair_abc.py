# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):

    string_S = ''
    new_string_b = ''
    new_string_c = ''
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0
    if (A == 0 and B == 0 and C == 0):
        return string_S
    elif (A <= 2 and B <= 2 and C <= 2):
        for i in range(A):
            string_S += 'a'
        for i in range(B):
            string_S += 'b'
        for i in range(C):
            string_S += 'b'
        return string_S
    else:
        while(A>0):
            string_S += 'a'
            A =A -1
        while(B>0):
            for i in range(len(string_S)):
                    new_string_b =

        return string_S


    return string_S
if __name__ == '__main__':

    print(solution(4,3,4))