class Solution:
    def myAtoi(self, str: str) -> int:
        str_leng = len(str)
        print(str_leng)
        ind = len(str) - len(str.lstrip())
        print(ind)
        if(str[ind].isalpha()):
            return 0
        else:
            k =ind
            str_new=''
            while str[k].isalpha() == False or k == str_leng:
                str_new += str[k]
                k =k+1

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            str = stringToString(line);
            print(str)
            ret = Solution().myAtoi(str)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()