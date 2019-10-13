def f(n, d):
    x = n * 9
    z = x
    k = 1
    while z % d:
        z = z * 10 + x
        k += 1
    return k, z / d


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        a, b = f(numerator, denominator)
        print(a, b)
        mod = numerator % denominator
        div = numerator / denominator
        if (numerator > denominator and mod == 0):
            dec = int(div)
        else:
            dec = div

        return (str(dec))


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
            numerator = int(line);
            line = next(lines)
            denominator = int(line);

            ret = Solution().fractionToDecimal(numerator, denominator)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()