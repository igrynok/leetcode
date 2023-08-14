class Solution(object):

    def get_directions(self, maze, current):
        rows = len(maze)
        columns = len(maze[0])
        directions = []

        up = current[0]
        while up - 1 >= 0 and maze[up - 1][current[1]] == 0:
            up -= 1
        if up != current[0]:
            directions.append(([up, current[1]], current[0] - up))

        down = current[0]
        while down + 1 <= rows - 1 and maze[down + 1][current[1]] == 0:
            down += 1
        if down != current[0]:
            directions.append(([down, current[1]], down - current[0]))

        right = current[1]
        while right + 1 <= columns - 1 and maze[current[0]][right + 1] == 0:
            right += 1
        if right != current[1]:
            directions.append(([current[0], right], right - current[1]))

        left = current[1]
        while left - 1 >= 0 and maze[current[0]][left - 1] == 0:
            left -= 1
        if left != current[1]:
            directions.append(([current[0], left], current[1] - left))

        return directions

    def dfs(self, maze, current, destination, visited, path):
        if current == destination:
            return path
        p = 10**8
        for cell, length in self.get_directions(maze, current):
            if tuple(cell) not in visited or (tuple(cell) in visited and visited[tuple(cell)] > path):
                visited[tuple(cell)] = path
                p = min(p, self.dfs(maze, cell, destination, visited, path + length))
        return p

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        visited = { tuple(start) : 0 }
        dist = self.dfs(maze, start, destination, visited, 0)
        return dist if dist != 10**8 else -1


if __name__ == '__main__':
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0,4]
    dest = [4,4]
    print(Solution().shortestDistance(maze, start, dest))