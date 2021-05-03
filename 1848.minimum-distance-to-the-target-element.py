from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        best = len(nums) + 10
        for i, x in enumerate(nums):
            if x != target:
                continue
            candidate = abs(i - start)
            if candidate > best:
                continue
            best = candidate

        return best


sol = Solution()
print(sol.getMinDistance(nums=[1, 2, 3, 4, 5], target=5, start=3))
print(sol.getMinDistance(nums=[1], target=1, start=0))
