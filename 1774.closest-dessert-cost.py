from typing import List


class Solution:
    def cmp(self, a, b, target):
        if abs(a - target) < abs(b - target):
            return a
        if abs(a - target) > abs(b - target):
            return b
        if a < b:
            return a
        return b

    def closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int
    ) -> int:
        topping_combos = set([0])
        for cost in toppingCosts:
            new_combos = set()
            for combo in topping_combos:
                new_combos.add(combo)
                new_combos.add(combo + cost)
                new_combos.add(combo + 2 * cost)
            topping_combos = new_combos

        combo_prices = sorted(list(topping_combos))
        best = baseCosts[0]

        combos = (a + b for a in combo_prices for b in baseCosts)
        for poss in combos:
            best = self.cmp(best, poss, target)

        return best


x = Solution()
assert x.closestCost(baseCosts=[1, 7], toppingCosts=[3, 4], target=10) == 10
assert x.closestCost(baseCosts=[2, 3], toppingCosts=[4, 5, 100], target=18) == 17
assert x.closestCost(baseCosts=[3, 10], toppingCosts=[2, 5], target=9) == 8
assert x.closestCost(baseCosts=[10], toppingCosts=[1], target=1) == 10
