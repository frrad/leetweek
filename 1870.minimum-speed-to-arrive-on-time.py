from typing import List


def hoursTaken(speed: int, dist: List[int]):
    if speed == 0 and len(dist) > 0:
        return float("inf")

    acc = 0
    for i, d in enumerate(dist):
        if i == len(dist) - 1:
            return acc + float(d) / float(speed)
        acc += d // speed
        if d % speed != 0:
            acc += 1


def worksFactory(dist, budget):
    def works(speed):
        return hoursTaken(speed, dist) <= budget

    return works


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        works = worksFactory(dist, hour)

        a, b = 1, 10_000_000
        if works(a):
            return 1
        if not works(b):
            return -1

        while b - a > 10:
            c = (b + a) // 2
            if works(c):
                b = c
            else:
                a = c

        for i in range(a, b + 1):
            if works(i):
                return i


sol = Solution()
print(sol.minSpeedOnTime(dist=[1, 3, 2], hour=6))
print(sol.minSpeedOnTime(dist=[1, 3, 2], hour=2.7))
print(sol.minSpeedOnTime(dist=[1, 3, 2], hour=1.9))
