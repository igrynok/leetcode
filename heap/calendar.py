import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        heap = [intervals[0][1]]

        for i in range(1, len(intervals)):

            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, intervals[i][1])

        return len(heap)


if __name__ == '__main__':
    s = Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]])
    print(s)
