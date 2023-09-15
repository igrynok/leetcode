# [[1, 1], [-1, 1]]
# True

# [[-1, -1], [1, 1]]
# False

# []
# ?

class Solution(object):

    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return False

        start_x, start_y = points[0][0], points[0][1]
        lines = set([x for [x, y] in points])

        for i in range(1, len(points)):
            x, y = points[i][0], points[i][1]
            if start_y != y:
                continue
            line = (start_x - x) / 2.0 + x
            lines.add(line)

        if not lines:
            return False

        for line in lines:

            pairs = set([(float(x), float(y)) for [x, y] in points])

            for point in points:

                if not pairs:
                    break

                x, y = float(point[0]), float(point[1])

                if (x, y) not in pairs:
                    continue

                if x == line:
                    pairs.remove((x, y))
                    continue

                if (x + 2 * (line - x), y) in pairs:
                    pairs.remove((x + 2 * (line - x), y))
                    pairs.remove((x, y))
                else:
                    break

            if not pairs:
                return True

        return False
