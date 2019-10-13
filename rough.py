def compute_score(number):
    dig = []
    score =0
    while(number>0):
        dig.append(number % 10)
        number = number//10
    dig = dig[::-1]
    five = 5
    three = 3
    count_five = 0
    count_three = 0
    count_odd = 0
    count_5 = 0
    for i in range(len(dig)):
        if five in dig:
            count_five +=1
        if three in dig:
            count_three +=1
        if dig[i]%2 !=0:
            count_odd +=1
    if count_three <2:
        count_three = 0
    #list_a = []
    k=1
    sum = 1
    score_1 =0
    while sum < len(dig):
        score_1 += k*k
        k = k+1
        sum += k
    print(score_1)
    if(number%5 ==0):
        count_5 = 1

    if(count_three==2 and count_five ==1):
        score = count_five * 2 + 4 + 6 + count_odd*1  +score_1
    elif (count_three == 2 and count_five != 1):
        score = count_five * 2 + 4 + count_odd*1  +score_1
    elif (count_three > 2 and count_five == 1):
        score = count_five * 2 + 4 + (count_three-2)*4 + count_odd*1  +score_1
    elif (count_three > 2 and count_five != 1):
        score = count_five * 2 +  4 + (count_three-2)*4 + count_odd*1  +score_1







    return score

if __name__ == "__main__":
    print(compute_score(101275345))
