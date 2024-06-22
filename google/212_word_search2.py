from collections import defaultdict
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefix_dict = defaultdict(list)
        for word in words:
            for i in range(word):
                prefix_dict[word[:i+1]].append(word)