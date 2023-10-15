# [[1, 4]]
# [[1, 4]]

# [[1,4],[4,5]]
# [[1, 5]]

# [[1,3],[2,6],[8,10],[15,18]]
# [[1,6],[8,10],[15,18]]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals

        intervals.sort()

        answer = [intervals[0][:]]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            prev = answer[-1]

            if prev[1] < interval[0] or interval[1] < prev[0]:
                answer.append(interval)
            else:
                start = min(prev[0], interval[0])
                end = max(prev[1], interval[1])
                answer[-1] = [start, end]

        return answer