class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        # if str1 == str2:
        #     return True

        dict_ = {}
        for i in range(len(str1)):
            if str1[i] not in dict_:
                dict_[str1[i]] = str2[i]
            else:
                if dict_[str1[i]] != str2[i]:
                    return False

        s= set(dict_.values())
        print(dict_)


        if len(dict_) == 26 and len(s) == 26:
            return False

        return True


s =Solution()
x = "abcdefghijklmnopqrstuvwxyz"
y = "bcdefghijklmnopqrstuvwxyzq"


str1 = 'abcdefghijklmnopqrstuvwxyz'
str2 = 'bcdefghijklmnopqrstuvwxyza'
print(s.canConvert(x,y))