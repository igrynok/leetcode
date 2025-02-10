from typing import List


class Solution:

    def get_neighbours(self, cell, image, old_color):
        neighbours = []
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for d in directions:
            new_cell = (cell[0] + d[0], cell[1] + d[1])
            if 0 <= new_cell[0] < len(image) and 0 <= new_cell[1] < len(image[0]):
                if image[new_cell[0]][new_cell[1]] == old_color:
                    neighbours.append((new_cell[0], new_cell[1]))

        return neighbours

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        old_color = image[sr][sc]
        if old_color == color:
            return image

        def dfs(cell):
            image[cell[0]][cell[1]] = color
            for n in self.get_neighbours(cell, image, old_color):
                dfs(n)

        dfs((sr, sc))

        return image