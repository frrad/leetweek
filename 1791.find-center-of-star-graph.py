class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cts = set()
        for x in [edges[0][0], edges[0][1], edges[1][0], edges[1][1]]:
            if x in cts:
                return x
            else:
                cts.add(x)


sol = Solution()
assert sol.findCenter(edges=[[1, 2], [2, 3], [4, 2]]) == 2
assert sol.findCenter(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
