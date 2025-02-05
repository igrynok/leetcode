from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        words1 = s1.split()
        words2 = s2.split()
        word_count = Counter(words1 + words2)

        return [key for key in word_count.keys() if word_count[key] == 1]