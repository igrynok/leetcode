class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def next_ch(word, index):
            skip = 0
            for i in range(index - 1, -1, -1):
                if word[i] == '#':
                    skip += 1
                    continue
                else:
                    if skip > 0:
                        skip -= 1
                        continue
                    else:
                        return word[i], i

            return "end", -1

        i, j = len(s), len(t)
        while i or j:

            s_next_ch, i = next_ch(s, i)
            t_next_ch, j = next_ch(t, j)

            if i == -1 and j == -1:
                return True
            elif i == -1 or j == -1:
                return False

            if s_next_ch and t_next_ch and s_next_ch == t_next_ch:
                continue
            else:
                return False

        return True