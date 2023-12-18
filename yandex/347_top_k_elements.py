# [1] k = 1
# [1]

# [1, 1, 1, 2, 2, 3] k = 2
# [1, 2]
from collections import Counter
from heapq import heappop, heapify


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        heap = []
        for num in counter.keys():
            heap.append((-counter[num], num))

        heapify(heap)

        answer = []
        for i in range(k):
            answer.append(heappop(heap)[1])

        return answer