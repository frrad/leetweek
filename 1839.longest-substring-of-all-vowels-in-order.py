vowels = list("aeiou")


def state_transition(state, next_state, first_char, i):
    if state == 4:
        if next_state == 4:
            return (4, first_char, -1)
        elif next_state == 0:
            return (0, i, i - first_char)
        else:
            return (-2, i, i - first_char)

    if next_state - state in (0, 1):
        return (next_state, first_char, -1)

    if next_state == 0:
        return (0, i, -1)

    return (-2, i, -1)


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        state = -2
        first_char = -1
        best = 0

        for i, x in enumerate(word + "a"):
            next_state = vowels.index(x)
            state, first_char, best_can = state_transition(
                state, next_state, first_char, i
            )
            if best_can > best:
                best = best_can

        return best


# sol = Solution()
# print(sol.longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
# print(sol.longestBeautifulSubstring("aeeeiiiioooauuuaeiou"))
# print(sol.longestBeautifulSubstring("a"))
