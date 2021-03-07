class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        reading = False
        read = 0

        for c in s:
            if c == "1" and reading:
                continue

            if c == "1" and not reading:
                reading = True
                read +=1

            if c == "0" and reading:
                reading = False

            if c == "0" and not reading:
                continue

            if read >1:
                return False

        return True

sol = Solution()

assert sol.checkOnesSegment("1001") == False
assert sol.checkOnesSegment("110") == True

