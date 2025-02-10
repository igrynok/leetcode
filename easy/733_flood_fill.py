from collections import deque
from typing import List


class Solution:

    def get_neighbours(self, cell, image, old_color):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        neighbours = []
        for d in directions:
            new_cell = (cell[0] + d[0], cell[1] + d[1])
            if  0 <= new_cell[0] < len(image) and 0 <= new_cell[1] < len(image[0]):
                if image[new_cell[0]][new_cell[1]] == old_color:
                    neighbours.append(new_cell)

        return neighbours

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        queue = deque([(sr, sc)])
        old_color = image[sr][sc]
        visited = set([(sr, sc)])
        image[sr][sc] = color
        while queue:
            node = queue.popleft()
            for n in self.get_neighbours(node, image, old_color):
                if n not in visited:
                    image[n[0]][n[1]] = color
                    queue.append(n)
                    visited.add(n)

        return image