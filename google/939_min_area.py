import math
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        points_set = set()

        for p in points:
            points_set.add(tuple(p))

        min_area = math.inf

        for i in range(len(points)):
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):

                x2, y2 = points[j]

                if x1 == x2 or y1 == y2:
                    continue

                if (x2, y1) in points_set and (x1, y2) in points_set:
                    min_area = min(min_area, abs(x2-x1)*abs(y2-y1))

        return min_area if min_area != math.inf else 0