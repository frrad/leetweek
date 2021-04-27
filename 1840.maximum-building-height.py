from typing import List


def rm_dom(restrictions, ends_at):
    if len(restrictions) == 0:
        return []

    restrictions.sort()

    curr = restrictions[0]
    ans = []

    for x in restrictions[1:]:
        if curr[1] - curr[0] > x[1] - x[0]:
            ans.append((curr, (x[0] - 1, curr[1] + x[0] - curr[0] - 1)))

            curr = x

    ans.append((curr, (ends_at, curr[1] + ends_at - curr[0])))

    return ans


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        leftwards = []
        rightwards = [(1, 0)]
        for starts, height in restrictions:
            rightwards.append((starts, height))
            leftwards.append((-starts, height))

        rightwards = rm_dom(rightwards, n)
        leftwards = rm_dom(leftwards, -1)

        leftwards = [((-c, d), (-a, b)) for ((a, b), (c, d)) in leftwards]
        leftwards.reverse()

        print(rightwards, leftwards)

        cuts = set()
        for x in (leftwards, rightwards):
            for ((a, b), (c, d)) in x:
                cuts.add(a)
                cuts.add(c)

        bops = list(cuts)
        bops.sort()
        segs = list(zip(bops[:-2], bops[1:]))

        print(segs)

        a = 1

        return 0


sol = Solution()
print(sol.maxBuilding(n=5, restrictions=[[2, 1], [4, 1]]))
print(sol.maxBuilding(n=6, restrictions=[]))
print(sol.maxBuilding(n=10, restrictions=[[5, 3], [2, 5], [7, 4], [10, 3]]))
