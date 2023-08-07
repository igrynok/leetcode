from collections import deque


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        max_dist = -1

        queue = deque()
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))

        if len(queue) == n*n:
            return -1

        levels = -1
        while queue:
            levels += 1
            level_nodes = len(queue)
            for i in range(level_nodes):
                node = queue.popleft()
                for child in self.get_neighbours(node, n):
                    if child in visited:
                        continue
                    queue.append(child)
                    visited.add(child)

        return levels

    def get_neighbours(self, coord, n):
        result = []
        current = coord[1] + coord[0] * 1j
        directions = (1, -1, 1j, -1j)

        for direction in directions:
            neighbour = current + direction
            row = int(neighbour.imag)
            column = int(neighbour.real)
            if 0 <= row < n and 0 <= column < n:
                result.append((row, column))

        return result


if __name__ == '__main__':
    print(Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
