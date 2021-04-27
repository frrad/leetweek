from typing import List


def total_cost(cost_through, nums, a, b):
    return cost_through[b] - cost_through[a] - a * (nums[b] - nums[a])


def costs(nums):
    level = nums[0]
    cost = 0
    cost_through = [cost]

    i = 1
    while i < len(nums):
        new_level = nums[i]
        cost += i * (new_level - level)
        cost_through.append(cost)
        level = new_level
        i += 1
    return cost_through


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        cost_through = costs(nums)

        best = 1

        a, b = 0, 0
        while b < len(nums):
            while (
                a < len(nums)
                and b < len(nums)
                and total_cost(cost_through, nums, a, b) <= k
            ):
                if 1 + b - a > best:
                    best = 1 + b - a
                b += 1

            while (
                a < len(nums)
                and b < len(nums)
                and total_cost(cost_through, nums, a, b) > k
            ):
                a += 1

        return best


# sol = Solution()
# print(sol.maxFrequency([1, 2, 4], 5))
# print(sol.maxFrequency([1, 4, 8, 13], 5))
# print(sol.maxFrequency([3, 9, 6], 2))
