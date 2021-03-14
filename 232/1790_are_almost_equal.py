class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diffs = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)

        if len(diffs) == 0:
            return True

        if len(diffs) != 2:
            return False

        a, b = diffs[0], diffs[1]
        return s1[a] == s2[b] and s1[b] == s2[a]


sol = Solution()
assert sol.areAlmostEqual(s1="bank", s2="kanb") == True
assert sol.areAlmostEqual(s1="attack", s2="defend") == False
assert sol.areAlmostEqual(s1="kelb", s2="kelb") == True
assert sol.areAlmostEqual(s1="abcd", s2="dcba") == False
