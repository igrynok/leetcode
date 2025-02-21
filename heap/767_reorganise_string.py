from collections import Counter
from heapq import heappush, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:

        counter = Counter(s)
        heap = []

        for ch, count in counter.items():
            heappush(heap, (-count, ch))

        reorg_s = []
        while heap:
            count1, ch1 = heappop(heap)
            if not reorg_s or reorg_s[-1] != ch1:
                reorg_s.append(ch1)
                if -count1 - 1 > 0:
                    heappush(heap, (count1 + 1, ch1))
            else:
                if not heap:
                    return ""
                count2, ch2 = heappop(heap)
                reorg_s.append(ch2)
                if -count2 - 1 > 0:
                    heappush(heap, (count2 + 1, ch2))
                heappush(heap, (count1, ch1))

        return "".join(reorg_s)