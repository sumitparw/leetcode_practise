def search_n(matrix,rowcount,columncount,targetvalue):
    i = 0

    # set indexes for top right element
    j = columncount - 1
    while (i < rowcount and j >= 0):

        if (mat[i][j] == targetvalue):
            return(i,j)

        if (mat[i][j] > targetvalue):
            j -= 1

        # if mat[i][j] < x
        else:
            i += 1
    return (-1, -1)
def binary_searchlogn_1(matrix,targetvalue):
    if len(matrix)==1:
        return 0
    start = 0
    end = len(matrix)-1
    while start<end:
        mid_row = (start+end)//2
        if matrix[mid_row][0]<=targetvalue and matrix[mid_row+1][0]>targetvalue:
            return mid_row
        if targetvalue < matrix[mid_row][0]:
            end =mid_row-1
        else:
            start=mid_row+1
    return start

def binary_searchlogn_2(row,targetrow,targetvalue):
    start =0
    end= len(row)-1
    while start<=end:
        mid = (start+end)//2
        if targetvalue == row[mid]:
            return (targetrow,mid)
        if targetvalue<row[mid]:
            end= mid-1
        else:
            start = mid+1
    return (-1,-1)
def search_logn(matrix,rowcount,columncount,targetvalue):
    if not matrix or not matrix[0]:
        return (-1,-1)
    target_row =binary_searchlogn_1(matrix,targetvalue)
    print(target_row)
    return binary_searchlogn_2(matrix[target_row],target_row,targetvalue)

def search_n2(matrix,rowcount,columncount,targetvalue):
    for i in range(rowcount):
        for j in range(columncount):
            if matrix[i][j]==targetvalue:
                return (i,j)
    return (-1,-1)

mat = [ [10, 20, 30, 40],
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ] 
#print(search_n2(mat, 4,4, 51))
#print(search_n(mat, 4,4, 51))
#print((2+3)//2)
print(search_logn(mat,4,4,51))