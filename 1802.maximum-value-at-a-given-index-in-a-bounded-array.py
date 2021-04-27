def triangle(n):
    return (n * (n + 1)) // 2


def smallest_side_of_hill(height, squares):
    if height >= squares:
        return triangle(height) - triangle(height - squares)
    return triangle(height) + (squares - height)


def smallest_hill(n, height, index):
    # print("left", smallest_side_of_hill(height, index + 1))
    # print("right", smallest_side_of_hill(height, n - index))
    return (
        smallest_side_of_hill(height, index + 1)
        + smallest_side_of_hill(height, n - index)
        - height
    )


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        a, b = 1, maxSum

        while b - a > 1:
            c = (a + b) // 2
            print(a, c, b)

            ms = smallest_hill(n, c, index)
            print(c, "<>", ms)
            if ms > maxSum:
                b = c
            elif ms < maxSum:
                a = c
            else:
                return c

        if smallest_hill(n, a, index) == maxSum:
            return a
        if smallest_hill(n, b, index) == maxSum:
            return b
        return a


sol = Solution()
print(sol.maxValue(n=4, index=2, maxSum=6))
print(sol.maxValue(n=6, index=1, maxSum=10))
