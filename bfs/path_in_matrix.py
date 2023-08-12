from collections import deque


class Solution(object):

    def get_neighbours(self, grid, cell):

        n = len(grid)
        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        neighbours = []
        for (x, y) in directions:
            row = cell[0] + y
            column = cell[1] + x
            if 0 <= row < n and 0 <= column < n:
                neighbours.append((row, column))
        return neighbours

    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        if grid[0][0] or grid[n-1][n-1] == 1:
            return -1

        if len(grid) == 1 and grid[0][0] == 0:
            return 1

        queue = deque([(0, 0)])
        visited = {(0, 0)}

        grid[0][0] = 1
        level = 1
        while len(queue) > 0:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in self.get_neighbours(grid, node):
                    if child in visited:
                        continue
                    if grid[child[0]][child[1]] == 0:
                        if child[0] == n - 1 and child[1] == n - 1:
                            return level
                        queue.append(child)
                        visited.add(child)

        return -1


if __name__ == '__main__':
    print(Solution().shortestPathBinaryMatrix([[0,1],[1,0]]))