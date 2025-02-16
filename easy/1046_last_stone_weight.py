from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            max1 = heappop(stones)
            max2 = heappop(stones)
            heappush(stones, max1 - max2)

        return -stones[0]