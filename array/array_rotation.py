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


def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1


# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    rverseArray(arr, 0, d - 1)
    rverseArray(arr, d, n - 1)
    rverseArray(arr, 0, n - 1)

def rotate_nl2r(arr,d):
    return arr[d:] + arr[:d]

def rotate_nr2l(arr,d):
    n = len(arr)
    return arr[n-d:] + arr[:n-d]

n_input = [2,4,5,6,7,8]
d = 2
print(rotate_nl2r(n_input,d))
print(rotate_nr2l(n_input,d))
leftRotate(n_input,d)
print(n_input)

