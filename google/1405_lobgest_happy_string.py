import heapq
from heapq import heapify


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heap = [(count, max_ch) for (count, max_ch) in heap if count != 0]
        heapify(heap)
        longest_str = ""

        while heap:
            count, ch = heapq.heappop(heap)
            if len(longest_str) >= 2 and longest_str[-2:] == ch * 2:
                if not heap:
                    break
                count2, ch2 = heapq.heappop(heap)
                longest_str += ch2
                count2 += 1
                if count2 < 0:
                    heapq.heappush(heap, (count2, ch2))
                heapq.heappush(heap, (count, ch))
            else:
                longest_str += ch
                count += 1
                if count < 0:
                    heapq.heappush(heap, (count, ch))

        return longest_str