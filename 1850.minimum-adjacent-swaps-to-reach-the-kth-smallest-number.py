def nextStr(num):
    last = num[-1]
    for i in range(2, len(num) + 1):
        if num[-i] < last:
            head = num[:-i]
            tail = num[-i:]
            return head + inc(tail)
        last = num[-i]


def inc(num: str) -> str:
    digits = [x for x in list(num)]
    original_first = digits[0]
    digits.sort()
    i = digits.index(original_first)
    while digits[i] <= original_first:
        i += 1
    first = digits.pop(i)
    digits = [first] + digits
    return "".join(digits)


def nextFour(x: str, k: int) -> str:
    for _ in range(k):
        x = nextStr(x)
    return x


def numSwaps(start: str, end: str) -> int:
    if start == end:
        return 0
    if len(start) == 0 or len(end) == 0:
        return 0
    if start[0] == end[0]:
        i = 0
        while start[i] == end[i]:
            i += 1
        return numSwaps(start[i:], end[i:])

    end_chars = list(end)
    i = end_chars.index(start[0])
    end_chars.pop(i)

    return i + numSwaps("".join(end_chars), start[1:])


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        return numSwaps(nextFour(num, k), num)


sol = Solution()
print(sol.getMinSwaps("5489355142", 4))
print(sol.getMinSwaps(num="11112", k=4))
print(sol.getMinSwaps(num="00123", k=1))
