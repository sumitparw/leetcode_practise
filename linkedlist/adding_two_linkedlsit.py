# Definition for singly-linked list.
import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        prev = None
        temp = None
        while l1 is not None or l2 is not None:
            l1_data = 0 if l1 is None else l1.val
            l2_data = 0 if l2 is None else l2.val

            sum = carry + l1_data + l2_data

            carry = 1 if sum > 10 else 0
            sum = sum if sum < 10 else sum % 10
            temp = ListNode(sum)

            if self.next == None:
                self = temp
            else:
                prev.next = temp
            prev = temp

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


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
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()