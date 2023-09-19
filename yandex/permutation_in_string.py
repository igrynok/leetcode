# "ab" "eidbaoooooo"
# True

# "ab" "eidboaoo"
# False
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        fast = 0
        counter = Counter(s1)
        count = 0

        while fast < n2 + 1:

            if count == n1:
                if Counter(s2[fast-n1:fast]) == counter:
                    return True
                else:
                    count -= 1

            if fast < n2 and s2[fast] in counter:
                count += 1
            else:
                count = 0

            fast += 1

        return False