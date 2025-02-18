import math
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        heap = [-g for g in gifts]
        heapify(heap)
        for i in range(k):
            gift = math.floor(math.sqrt(-heappop(heap)))
            heappush(heap, -gift)

        return -sum(heap)