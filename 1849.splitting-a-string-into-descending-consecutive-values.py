def splitDescStartsWith(s: str, x: int) -> bool:
    if len(s) == 0:
        return True
    for i in range(1, len(s) + 1):
        head = int(s[:i])
        if head == x and splitDescStartsWith(s[i:], x - 1):
            return True
        if head > x:
            return False
    return False


class Solution:
    def splitString(self, s: str) -> bool:
        for i in range(1, len(s)):
            head = int(s[:i])
            tail = s[i:]
            if splitDescStartsWith(tail, head - 1):
                return True
        return False


sol = Solution()
print(sol.splitString(s="1234"))
print(sol.splitString(s="050043"))
print(sol.splitString(s="9080701"))
print(sol.splitString(s="10009998"))
print(sol.splitString(s="200100"))
