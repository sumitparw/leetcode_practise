def first_set_bit(n):
    x = "{0:b}".format(n)
    for i in range(len(x) - 1, -1, -1):
        if x[i] == '1':
            print(len(x) - i)
            break


if __name__ == "__main__":
    n = int(input())
    if (n == 0):
        print(0)
    else:
        for i in range(n):
            first_set_bit(int(input()))


