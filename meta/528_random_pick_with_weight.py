from random import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.distr = []
        for index, weight in enumerate(w):
            for i in range(weight):
                self.distr.append(index)

    def pickIndex(self) -> int:
        index = random.randint(0, len(self.distr) - 1)
        return self.distr[index]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()