class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mins = {}
        for us_id, tim in logs:
            if us_id not in mins:
                mins[us_id] = set()
            mins[us_id].add(tim)

        ans = [0] * k
        for us in mins:
            heh = len(mins[us])
            if heh > k:
                continue
            ans[heh - 1] += 1
        return ans
