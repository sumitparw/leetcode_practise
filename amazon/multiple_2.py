
def mult_loop(n):
    mul =  2
    number = 2
    while(number<=n):
        number = number*mul
        if(number == n):
            return True
            break
        else:
            continue
    return False
def div_loop(n):
    div = 2
    number = n
    while (number >= 2):
        number = number / div
        if (number == 2):
            return True
            break
        else:
            continue
    return False
def bitwise_operation(n):
    if((n & n-1)==0):
        return True
    else:
        return False


if __name__ =="__main__":
    n = 66
    print(mult_loop(n))
    print(div_loop(n))
    print(bitwise_operation(n))
