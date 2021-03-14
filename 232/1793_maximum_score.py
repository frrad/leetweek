class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        a, b = k, k
        best, level = nums[k], nums[k]
        while True:
            L, R = -1, -1
            if a > 0:
                L = nums[a - 1]
            if b < len(nums) - 1:
                R = nums[b + 1]

            if L == -1 and R == -1:
                return best

            if L > R:
                a -= 1
            else:
                b += 1

            level = min([nums[a], level, nums[b]])
            best = max(best, level * (b - a + 1))


sol = Solution()
assert sol.maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3) == 15
assert sol.maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0) == 20
assert (
    sol.maximumScore(
        nums=[6569, 9667, 3148, 7698, 1622, 2194, 793, 9041, 1670, 1872], k=5
    )
    == 9732
)
