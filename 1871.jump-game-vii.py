from typing import Dict


memo: Dict[int, bool] = dict()
bin_str: str = ""


def reach(i: int, minJump: int, maxJump: int):

    if i in memo:
        return memo[i]

    if minJump >= i:
        memo[i] = False
        return False

    if bin_str[0] != "0":
        memo[i] = False
        return False

    if bin_str[i - 1] != "0":
        memo[i] = False
        return False

    if minJump <= i - 1 <= maxJump:
        memo[i] = True
        return True

    for x in range(maxJump, minJump - 1, -1):
        if reach(i - x, minJump, maxJump):
            memo[i] = True
            return True

    memo[i] = False
    return False


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        global bin_str
        bin_str = s
        global memo
        memo = dict()

        return reach(len(s), minJump, maxJump)


sol = Solution()
print(sol.canReach(s="011010", minJump=2, maxJump=3))
print(sol.canReach(s="01101110", minJump=2, maxJump=3))
print(sol.canReach(s="0000000000", minJump=8, maxJump=8))
