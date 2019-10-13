def panagram(input1):
   list_ = []
   for i in range(26):
       list_.append(False)
   for k in input1.lower():
       if k !=" ":
           list_[ord(k) - ord('a')] =True
   if False in list_:
       return False
   else:
       return True
def panagram_set(input1):
    input = input1.lower()
    input = input.strip()
    input = set(input)
    #print(input)
    #alpha = []
    # for ch in input:
    #     if ord(ch)in range(ord('a'), ord('z')+1):
    #         alpha.append(ch)
    alpha = [ch for ch in input if ord(ch) in range(ord('a'), ord('z') + 1)]
    #print(alpha)
    if len(alpha) == 26:
        return 'true'
    else:
        return 'false'


if __name__ =="__main__":
    input1 = 'The quick brown fox jumps over the lazy dog'
    print(panagram(input1))
    print(panagram_set(input1))
    #print(ord('d')-ord('a'))
