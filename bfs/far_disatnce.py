from collections import deque


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        max_dist = -1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    max_dist = max(self.bfs((i, j), grid, n), max_dist)

        return max_dist

    def bfs(self, coord, grid, n):

        queue = deque([coord])
        min_dist = 1000
        visited = {coord}

        while queue:
            node = queue.popleft()
            for child in self.get_neighbours(node, n):
                if child in visited:
                    continue
                if grid[child[0]][child[1]] == 1:
                    dist = abs(child[0] - coord[0]) + abs(child[1] - coord[1])
                    if dist == 1:
                        return 1
                    else:
                        min_dist = min(min_dist, dist)
                visited.add(child)
                queue.append(child)

        return min_dist if min_dist != 1000 else -1

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
