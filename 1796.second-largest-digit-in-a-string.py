class Solution:
    def secondHighest(self, s: str) -> int:
        lol = set()
        for x in s:
            try:
                asdf = int(x)
                lol.add(asdf)
            except:
                pass

        qwer = list(lol)
        qwer.sort(reverse=True)
        if len(qwer) < 2:
            return -1
        return qwer[1]


sol = Solution()
print(sol.secondHighest(s="dfa12321afd"))
print(sol.secondHighest(s="abc1111"))
