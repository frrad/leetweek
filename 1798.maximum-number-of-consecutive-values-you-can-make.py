from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ans = 0
        for x in coins:
            if x > ans + 1:
                return ans + 1
            ans += x

        return ans + 1


sol = Solution()
print(sol.getMaximumConsecutive(coins=[1, 3]))
print(sol.getMaximumConsecutive(coins=[1, 1, 1, 4]))
print(sol.getMaximumConsecutive(coins=[1, 4, 10, 3, 1]))
