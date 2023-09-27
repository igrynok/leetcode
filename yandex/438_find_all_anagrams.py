# "a" "c"
# []

# "a" "a"
# [0]

# "cbaebabacd"
# "abc"

# "abab"
# "ab"


from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_counts = Counter(p)
        answer = []

        for i in range(len(s)):

            if s[i] not in p_counts:
                continue

            if i + len(p) <= len(s):
                s_counts = Counter(s[i:i + len(p)])
                if s_counts == p_counts:
                    answer.append(i)

        return answer