#annagram
from collections import Counter

def anagram_sort(input1,input2):
    if sorted(input1) == sorted(input2):
        return  True
    else:
        return False
def anagram_cnter(input1, input2):
    print(max(Counter(input2)))
    return Counter(input1) == Counter(input2)
def my_method(imput1,input2):
    list_1 = [0]*26
    list_2 = [0]*26
    val = 0
    for i in range(len(input1)):
          val = ord(input1[i])-ord('a')
          list_1[val] += 1
    val = 0
    for i in range(len(input2)):
          val = ord(input2[i])-ord('a')
          list_2[val] += 1
    print(list_1)
    print(list_2)
    if list_1 == list_2:
        return True
    else:
        return False


if __name__ =="__main__":
    input1 = 'abcda'
    input2 = 'dcab'
    print(anagram_cnter(input1,input2))
    #print(anagram_sort(input1,input2))
    #print(div_loop(n))
    print(Counter(input1))
   # print(my_method(input1,input2))

