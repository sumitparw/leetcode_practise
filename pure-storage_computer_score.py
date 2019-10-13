def compute_number_score(number):
    number_score =0
    prev =False
    seq_length = 1
    remainder_prev = -10
    if int(number%3==0):
        number_score +=4
    while number>0:
        remainder = int(number%10)
        number = int(number/10)
        if remainder == 7:
            number_score +=5
        if remainder%2 ==0:
            number_score+=3
        if remainder ==2 and prev == True:
            number_score +=6
        if remainder ==2:
            prev =True
        else:
            prev = False
        if remainder_prev == -10:
            remainder_prev = remainder
        else:
            if remainder == remainder_prev + 1:
                seq_length += 1
                remainder_prev = remainder
            else:
                number_score += seq_length * seq_length
                seq_length = 1
                remainder_prev = remainder
    if seq_length > 1:
        number_score += seq_length*seq_length
    return number_score

if __name__ == '__main__':
    input = 58488314
    print(compute_number_score(22222))
