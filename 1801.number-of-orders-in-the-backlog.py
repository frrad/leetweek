import heapq


def process(order, buys, sell):
    if order[2] == 1:
        # sell
        heapq.heappush(sell, (order[0], order[1]))
    if order[2] == 0:
        # buy
        heapq.heappush(buys, (-order[0], order[1]))

    keep = True
    while keep:
        if len(buys) == 0 or len(sell) == 0:
            break

        top_sell = heapq.heappop(sell)
        top_buy = heapq.heappop(buys)

        buy_price, sell_price = -top_buy[0], top_sell[0]

        if buy_price >= sell_price:
            if top_buy[1] > top_sell[1]:
                heapq.heappush(buys, (top_buy[0], top_buy[1] - top_sell[1]))
                continue
            elif top_buy[1] < top_sell[1]:
                heapq.heappush(sell, (top_sell[0], top_sell[1] - top_buy[1]))
                continue
            else:
                continue

        else:
            heapq.heappush(sell, top_sell)
            heapq.heappush(buys, top_buy)
            break


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buys = []
        sells = []

        for order in orders:
            process(order, buys, sells)

        ans = sum([x[1] for x in buys]) + sum([x[1] for x in sells])
        return ans % (10 ** 9 + 7)


sol = Solution()
assert (
    sol.getNumberOfBacklogOrders([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]) == 6
)
assert (
    sol.getNumberOfBacklogOrders(
        [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
    )
    == 999999984
)
