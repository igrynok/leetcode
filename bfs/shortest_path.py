from collections import deque


class Solution(object):

    def get_neibhours(self, node, grid, value=None):

        answer = []
        directions = [1, -1, 1j, -1j]
        node_compl = node[1] + node[0] * 1j
        n = len(grid)

        for direction in directions:

            neighbour = node_compl + direction
            x = int(neighbour.real)
            y = int(neighbour.imag)

            if 0 <= x < n and 0 <= y < n:
                if value is None:
                    answer.append((x, y))
                elif grid[y][x] == value:
                    answer.append((y, x))

        return answer

    def find_island(self, grid):

        n = len(grid)
        start = (-1, -1)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start[0] != -1:
                break

        queue = deque([start])
        visited = {start}
        while queue:
            node = queue.popleft()
            for child in self.get_neibhours(node, grid, 1):
                if child in visited:
                    continue
                queue.append(child)
                visited.add(child)

        return list(visited)

    def bfs(self, cell, grid, island):

        queue = deque([cell])
        visited = {cell}
        level = -1

        while queue:
            level += 1
            for i in range(len(queue)):
                node = queue.popleft()
                for child in self.get_neibhours(node, grid):
                    if child in visited:
                        continue
                    if grid[child[0]][child[1]] == 1 and child not in island:
                        return level
                    queue.append(child)
                    visited.add(child)

        return level

    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        island = self.find_island(grid)

        shortest_path = 222
        for cell in island:
            shortest_path = min(self.bfs(cell, grid, island), shortest_path)

        return shortest_path


if __name__ == '__main__':
    input = [[0,1,0,0,0,0],[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0]]
    print(Solution().shortestBridge(input))
