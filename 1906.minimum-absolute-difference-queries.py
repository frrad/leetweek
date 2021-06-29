from typing import List
import sortedcontainers


def solve(nums, i, z):
    heh = sortedcontainers.SortedList()
    best = float("inf")

    for j in range(i, z + 1):
        adding = nums[j]

        a = heh.bisect_left(adding)
        if 0 <= a + 1 <= len(heh) - 1:
            right = heh[a + 1]
            if right == adding:
                continue
            else:
                test = abs(adding - heh[a])
                if test < best:
                    best = test

        if 0 <= a <= len(heh) - 1:
            test = abs(adding - heh[a])
            if test < best:
                best = test

        heh.add(adding)

    return -1 if best == float("inf") else best


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ans = []

        for a, b in queries:
            ans.append(solve(nums, a, b))
        return ans


sol = Solution()
print(sol.minDifference(nums=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [2, 3], [0, 3]]))


print(
    sol.minDifference(
        nums=[4, 5, 2, 2, 7, 10], queries=[[2, 3], [0, 2], [0, 5], [3, 5]]
    )
)
