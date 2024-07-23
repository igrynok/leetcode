from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        turns = {"right":"down", "down":"left", "left":"up", "up":"right"}
        navigation = {"right": (1, 0), "down":(0, 1), "left":(-1, 0), "up":(0, -1)}

        result = [matrix[0][0]]
        direction = "right"
        position = (0, 0)
        visited = {(0, 0)}

        while True:
            delta = navigation[direction]
            new_position = (position[0] + delta[0], position[1] + delta[1])
            if 0 <= new_position[0] < len(matrix[0]) and 0 <= new_position[1] < len(matrix) and new_position not in visited:
                result.append(matrix[new_position[1]][new_position[0]])
                position = new_position
                visited.add(new_position)
            else:
                direction = turns[direction]
                delta = navigation[direction]
                new_position = (position[0] + delta[0], position[1] + delta[1])
                if new_position in visited:
                    break

        return result