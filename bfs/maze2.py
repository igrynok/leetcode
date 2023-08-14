from collections import deque


class Solution(object):

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        rows, columns = len(maze), len(maze[0])
        queue = deque([start])
        dist = [[float('inf') for _ in range(columns)] for _ in range(rows)]
        dist[start[0]][start[1]] = 0

        while queue:

            node = queue.popleft()

            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:

                x, y, total = node[1], node[0], dist[node[0]][node[1]]
                while (0 <= x + direction[1] < columns and 0 <= y + direction[0] < rows) and maze[y + direction[0]][x + direction[1]] == 0:
                    x += direction[1]
                    y += direction[0]
                    total += 1

                if dist[y][x] > total:
                    dist[y][x] = total
                    queue.append((y, x))

        answer = dist[destination[0]][destination[1]]
        return answer if answer != float('inf') else -1


if __name__ == '__main__':
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0,4]
    dest = [4,4]
    print(Solution().shortestDistance(maze, start, dest))