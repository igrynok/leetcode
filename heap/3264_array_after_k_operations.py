from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        heap = [(num, index) for index, num in enumerate(nums)]
        heapify(heap)

        for _ in range(k):
            min_num, i = heappop(heap)
            heappush(heap, (min_num * multiplier, i))

        for h, i in heap:
            nums[i] = h

        return nums