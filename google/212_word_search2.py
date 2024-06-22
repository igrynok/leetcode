from collections import defaultdict
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        prefix_dict = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                prefix_dict[word[:i + 1]].append(word)

        answer = []

        def dfs(prefix, cell, visited):

            if not prefix in prefix_dict:
                return
            elif prefix in prefix_dict[prefix]:
                answer.append(prefix)
                return

            dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for d in dirs:
                if 0 <= cell[0] + d[0] < len(board[0]) and 0 <= cell[1] + d[1] < len(board) and not (cell[0] + d[0],
                                                                                                     cell[1] + d[
                                                                                                         1]) in visited:
                    new_cell = (cell[0] + d[0], cell[1] + d[1])
                    visited.add(new_cell)
                    dfs(prefix + board[new_cell[1]][new_cell[0]], new_cell, visited)

        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = (j, i)
                dfs(board[i][j], cell, set())

        return answer
