from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        words1 = s1.split()
        word_count1 = Counter(words1)
        words2 = s2.split()
        word_count2 = Counter(words2)

        uncommon = []
        for w1 in words1:
            if word_count1[w1] == 1 and w1 not in word_count2:
                uncommon.append(w1)
        for w2 in words2:
            if word_count2[w2] == 1 and w2 not in word_count1:
                uncommon.append(w2)

        return uncommon