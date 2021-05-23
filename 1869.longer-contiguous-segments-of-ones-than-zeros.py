class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest = {"1": 0, "0": 0}

        last = "X"
        cur_len = 0
        for x in s + "X":
            if x == last:
                cur_len += 1
                continue

            if last in longest and cur_len > longest[last]:
                longest[last] = cur_len
            cur_len = 1
            last = x

        return longest["1"] > longest["0"]


sol = Solution()
print(sol.checkZeroOnes("1101"))
print(sol.checkZeroOnes("111000"))
print(sol.checkZeroOnes("110100010"))
