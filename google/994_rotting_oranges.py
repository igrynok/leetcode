from collections import deque
from typing import List


class Solution:

    def get_neighbours(self, node, grid):

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neigbours = []
        for d in directions:
            if 0 <= d[0] + node[0] < len(grid) and 0 <= d[1] + node[1] < len(grid[0]):
                candidate = ((d[0] + node[0], d[1] + node[1]))
                if grid[candidate[0]][candidate[1]] == 1:
                    neigbours.append(candidate)

        return neigbours

    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = []

        is_left = False
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    rotten.append((row, column))
                if grid[row][column] == 1:
                    is_left = True

        if not rotten and not is_left:
            return 0

        queue = deque(rotten)
        time = -1

        while queue:
            time += 1
            num = len(queue)
            for _ in range(num):
                node = queue.popleft()
                neigbours = self.get_neighbours(node, grid)
                if neigbours:
                    for n in neigbours:
                        grid[n[0]][n[1]] = 2
                        queue.append((n[0], n[1]))

        is_left = False
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    is_left = True
                    break

        return time if not is_left else -1
