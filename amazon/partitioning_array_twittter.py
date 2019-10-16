def solve(k, numbers):
    # Write your code here
    freq = {}
    n = len(numbers)
    if(n%k == 0):
        dd = n/k
        count = 0
        for item in numbers:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        for key,value in freq.items():
            if value <=dd:
                count += value
            else:
                return "No"
        if count == n:
            return "Yes"
    else:
        return "No"

if __name__ =="__main__":
    k =3
    numbers =[3,6,4,8,8,8,6,4]

    print(solve(k,numbers))
