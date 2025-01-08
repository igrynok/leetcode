from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if len(matrix) == 1:
            return [elem for elem in matrix[0]]

        turns = {"right":"down", "down":"left", "left":"up", "up":"right"}
        navigation = {"right": (1, 0), "down":(0, 1), "left":(-1, 0), "up":(0, -1)}

        result = [matrix[0][0]]
        direction = "right"
        position = (0, 0)
        matrix[0][0] = 101

        while True:
            delta = navigation[direction]
            x, y = (position[0] + delta[0], position[1] + delta[1])
            if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix) and matrix[y][x] != 101:
                result.append(matrix[y][x])
                position = (x, y)
                matrix[y][x] = 101
            else:
                direction = turns[direction]
                delta = navigation[direction]
                x, y = (position[0] + delta[0], position[1] + delta[1])
                if x < 0 or x >= len(matrix[0]) or matrix[y][x] == 101:
                    break

        return result