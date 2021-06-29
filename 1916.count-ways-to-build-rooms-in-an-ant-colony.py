from typing import List
import functools

desc = dict()


def descendents(children, ix):
    if ix not in children:
        return 1

    if ix in desc:
        return desc[ix]

    ans = 1
    for chi in children[ix]:
        ans += descendents(children, chi)

    desc[ix] = ans
    return ans


order_memo = dict()


def orders(children, ix):
    if ix not in children:
        return 1

    if len(children[ix]) == 1:
        order_memo[ix] = orders(children, children[ix][0])
        return order_memo[ix]

    kids = [(orders(children, x), descendents(children, x)) for x in children[ix]]
    this_ans = functools.reduce(comb, kids)
    order_memo[ix] = this_ans[0]

    return this_ans[0]


def comb(a, b):
    (orders_a, descendents_a) = a
    (orders_b, descendents_b) = b
    total_desc = descendents_a + descendents_b
    return (choose(total_desc, descendents_b) * orders_a * orders_b, total_desc)


choose_memo = dict()


def choose(n, k):

    if n <= 1:
        return 1
    if n == k or k == 0:
        return 1

    ans = choose(n - 1, k - 1) + choose(n - 1, k)
    choose_memo[(n, k)] = ans
    return ans


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        children = dict()
        for i, parent in enumerate(prevRoom):
            if parent == -1:
                continue
            if parent not in children:
                children[parent] = []
            children[parent].append(i)

        return orders(children, 0)


sol = Solution()
print(sol.waysToBuildRooms(prevRoom=[-1, 0, 1]))
print(sol.waysToBuildRooms(prevRoom=[-1, 0, 0, 1, 2]))
