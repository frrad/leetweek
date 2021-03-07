from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        start = sum(nums)
        to_go = goal - start

        sgn = 1
        if to_go < 0:
            sgn = -1

        q = to_go // (sgn * limit)

        to_go -= q * (sgn * limit)
        if to_go != 0:
            return q + 1
        return q


sol = Solution()
assert sol.minElements(nums=[1, -1, 1], limit=3, goal=-4) == 2
assert sol.minElements(nums=[1, -10, 9, 1], limit=100, goal=0) == 1
