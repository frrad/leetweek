from typing import List


class Solution:
    def matcher(self, key, val):
        ix = ["type", "color", "name"].index(key)
        return lambda x: x[ix] == val

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule = self.matcher(ruleKey, ruleValue)
        return sum([rule(i) for i in items])


x = Solution()
ex1 = {
    "items": [
        ["phone", "blue", "pixel"],
        ["computer", "silver", "lenovo"],
        ["phone", "gold", "iphone"],
    ],
    "ruleKey": "color",
    "ruleValue": "silver",
}

ex2 = {
    "items": [
        ["phone", "blue", "pixel"],
        ["computer", "silver", "phone"],
        ["phone", "gold", "iphone"],
    ],
    "ruleKey": "type",
    "ruleValue": "phone",
}

print("ex1", x.countMatches(**ex1))
print("ex2", x.countMatches(**ex2))
