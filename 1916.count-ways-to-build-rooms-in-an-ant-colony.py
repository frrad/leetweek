from typing import List
import functools


def orders_descendents(ix):
    if ix not in children:
        return (1, 1)

    if ix in memo:
        return memo[ix]

    kids = [orders_descendents(x) for x in children[ix]]

    (kid_order, kid_desc) = functools.reduce(comb, kids)
    memo[ix] = (kid_order, kid_desc + 1)

    return memo[ix]


def comb(a, b):
    (orders_a, descendents_a) = a
    (orders_b, descendents_b) = b
    total_desc = descendents_a + descendents_b
    ans = (choose(total_desc, descendents_b) * orders_a * orders_b, total_desc)

    return ans


# i'm lazy..
# https://github.com/scipy/scipy/blob/701ffcc8a6f04509d115aac5e5681c538b5265a2/scipy/special/_comb.pyx#L5
def choose(N, k):
    if k > N or N < 0 or k < 0:
        return 0

    M = N + 1
    nterms = min(k, N - k)

    numerator = 1
    denominator = 1
    for j in range(1, nterms + 1):
        numerator *= M - j
        denominator *= j

    return numerator // denominator


def build_children(prevRoom):

    for i, parent in enumerate(prevRoom):
        if parent == -1:
            continue
        if parent not in children:
            children[parent] = []
        children[parent].append(i)


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        global children, memo
        children = dict()
        memo = dict()

        build_children(prevRoom)

        return orders_descendents(0)[0] % (10 ** 9 + 7)


sol = Solution()
print(sol.waysToBuildRooms(prevRoom=[-1, 0, 1]))
print(sol.waysToBuildRooms(prevRoom=[-1, 0, 0, 1, 2]))
print(sol.waysToBuildRooms(prevRoom=[-1, 0, 1, 0, 0, 2, 0, 5, 2, 6]))
