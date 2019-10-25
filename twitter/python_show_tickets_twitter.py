

def waitingTime(tickets, p):
    # Write your code here
    cnt = 0
    min_ =min(tickets)
    print(min_)
    for i in range(len(tickets)):
        if(tickets[p]!=0):
            tickets[i] = tickets[i] - min_
            cnt+=min_
        else:
            break
    while(tickets[p]!=0):
        for i in range(len(tickets)):
            if(tickets[i] == 0):
                continue
            else:
                tickets[i] -= 1
                cnt += 1
    return cnt

def method_2(tickets,p):
    count = 0
    delta = 0
    for i in range(len(tickets)):
        if tickets[i] < tickets[p]:
            delta += tickets[p] - tickets[i]
            if i > p:
                delta -= 1

    count = len(tickets) * (tickets[p] - 1) + (p + 1) - delta

    return count
def waitingTime(tickets, p):
    total_steps = tickets[p]
    first_half = tickets[:p]
    second_half = tickets[p+1:]

    for num in first_half:
        if num < tickets[p]:
            total_steps += num
        else:
            total_steps += tickets[p]

    for num in second_half:
        if num < tickets[p]:
            total_steps += num
        else:
            total_steps += tickets[p] - 1

    return total_steps
if __name__ =="__main__":
    p =2
    tickets  =[2, 6, 3, 4,5]

    print(waitingTime(tickets,p))