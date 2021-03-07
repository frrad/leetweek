class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if not works(nums1, nums2):
            return -1

        x, y = convert(nums1), convert(nums2)

        if count(x) > count(y):
            x, y = y, x

        moves = 0
        while count(x) != count(y):
            diff = count(y) - count(x)
            a, b = min(x.keys()), max(y.keys())
            most_increase = 6 - a
            most_decrease = b - 1
            if most_increase >= diff or most_decrease >= diff:
                return moves + 1

            if most_increase > most_decrease:
                x[a] -= 1
                if x[a] == 0:
                    del x[a]
                if 6 not in x:
                    x[6] = 0
                x[6] += 1
            else:
                y[b] -= 1
                if y[b] == 0:
                    del y[b]
                if 1 not in y:
                    y[1] = 0
                y[1] += 1

            moves += 1

        return moves


def count(x):
    ans = 0
    for k in x:
        ans += k * x[k]
    return ans


def works(nums1, nums2):
    a, b = len(nums1), len(nums2)
    if a > b:
        a, b = b, a
    return a <= b and b <= 6 * a


def convert(x):
    a = {}
    for i in x:
        if i not in a:
            a[i] = 0
        a[i] += 1
    return a


sol = Solution()
assert sol.minOperations(nums1=[1, 2, 3, 4, 5, 6], nums2=[1, 1, 2, 2, 2, 2]) == 3
assert sol.minOperations(nums1=[1, 1, 1, 1, 1, 1, 1], nums2=[6]) == -1
assert sol.minOperations(nums1=[6, 6], nums2=[1]) == 3
assert sol.minOperations(nums1=[2, 3], nums2=[5]) == 0
