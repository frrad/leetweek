from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best, prev, now = 0, 0, 0

        for x in nums:
            if x > prev:
                now += x
            else:
                now = x

            prev = x
            if now > best:
                best = now

        return best


sol = Solution()
print(sol.maxAscendingSum([10, 20, 30, 5, 10, 50]), 65)
print(sol.maxAscendingSum([10, 20, 30, 40, 50]), 150)
print(sol.maxAscendingSum([12, 17, 15, 13, 10, 11, 12]), 33)
print(sol.maxAscendingSum([100, 10, 1]), 100)
