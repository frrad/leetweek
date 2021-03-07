class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        return [0]


sol = Solution()
assert sol.getCollisionTimes(cars=[[1, 2], [2, 1], [4, 3], [7, 2]]) == [
    1.00000,
    -1.00000,
    3.00000,
    -1.00000,
]
assert sol.getCollisionTimes(cars=[[3, 4], [5, 4], [6, 3], [9, 1]]) == [
    2.00000,
    1.00000,
    1.50000,
    -1.00000,
]
