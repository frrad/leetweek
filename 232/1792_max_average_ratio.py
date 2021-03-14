import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [self.entry(x[0], x[1]) for x in classes]
        heapq.heapify(h)

        for x in range(extraStudents):
            best = heapq.heappop(h)
            heapq.heappush(h, self.entry(best[1] + 1, best[2] + 1))

        return sum([float(x[1]) / float(x[2]) for x in h]) / float(len(h))

    def entry(self, x, y):
        return (-self.benefit(x, y), x, y)

    def benefit(self, x, y):
        current = float(x) / float(y)
        if_add = float(x + 1) / float(y + 1)
        return if_add - current


sol = Solution()
x = sol.maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2)
print(x)
x = sol.maxAverageRatio(classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4)
print(x)
