import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_nums = sorted(nums1)

        running = 0
        best_improvement = 0
        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            running += diff

            gain = 0

            a = bisect.bisect_left(sorted_nums, nums2[i])

            gain = diff

            if a < len(sorted_nums):
                best = sorted_nums[a]
                gain = min(gain, abs(best - nums2[i]))

            if a > 0:
                best = sorted_nums[a - 1]
                gain = min(gain, abs(best - nums2[i]))

            best_improvement = max(best_improvement, diff - gain)

        return (running - best_improvement) % (10 ** 9 + 7)
