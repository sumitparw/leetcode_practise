def rotation(list_):
    for i in range(len(list_)):

        if (len(list_) == 1):
            break
        else:
            temp = list_[len(list_) - 1]
            del list_[len(list_) - 1]
            list_ = [temp] + list_
            if (-1 * (-i - 1) > len(list_)):
                del list_[0]
            else:
                del list_[-i - 1]
    print(list_[0])


n_input = input()
list_1 = []
for i in range(int(n_input)):
    n = input()
    list_ = input().split(" ")
    rotation(list_)

