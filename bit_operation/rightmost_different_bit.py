def rightmost_different_bit(m , n):
    x = "{0:b}".format(m)
    y = "{0:b}".format(n)
    print(x,y)
    for i in range(max(len(x),len(y))-1,-1,-1):
        if x[i] !=y[i]:
            return (len(x) - i)
            break


if __name__ == "__main__":
    m = 11
    n = 9
    print(rightmost_different_bit(m,n))


