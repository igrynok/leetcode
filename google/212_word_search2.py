from collections import defaultdict
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        prefix_dict = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                prefix_dict[word[:i + 1]].add(word)

        answer = []

        def dfs(prefix, cell):

            if not prefix in prefix_dict:
                return
            elif prefix in prefix_dict[prefix]:
                answer.append(prefix)
                for i in range(len(prefix)):
                    prefix_dict[prefix[:i + 1]].remove(prefix)

            letter = board[cell[1]][cell[0]]
            dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            board[cell[1]][cell[0]] = '#'
            for d in dirs:
                if 0 <= cell[0] + d[0] < len(board[0]) and 0 <= cell[1] + d[1] < len(board):
                    new_cell = (cell[0] + d[0], cell[1] + d[1])
                    dfs(prefix + board[new_cell[1]][new_cell[0]], new_cell)
            board[cell[1]][cell[0]] = letter

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board[i][j], (j, i))

        return answer
