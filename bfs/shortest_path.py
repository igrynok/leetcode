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
                if value is None or grid[y][x] == value:
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

    def bfs(self, grid, island):

        queue = deque()

        for cell in island:
            queue.append(cell)

        visited = set(island)
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

        shortest_path = self.bfs(grid, island)

        return shortest_path


if __name__ == '__main__':
    input = [[0,1,0,0,0,0],[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0]]
    print(Solution().shortestBridge(input))
