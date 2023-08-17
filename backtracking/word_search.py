class Solution(object):

    def get_neighbours(self, cell, board):

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        columns = len(board[0])
        rows = len(board)
        neighbours = []
        for dirs in directions:
            column = cell[0] + dirs[0]
            row = cell[1] + dirs[1]
            if 0 <= column < columns and 0 <= row < rows:
                neighbours.append((column, row))

        return neighbours

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        starts = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    starts.append((j, i))

        if starts and len(word) == 1:
            return True

        def dfs(index, cell):
            if index == (len(word) - 1) and word[index] == board[cell[1]][cell[0]]:
                return True
            for child in self.get_neighbours(cell, board):
                if child in visited:
                    continue
                if index + 1 <= len(word) and board[child[1]][child[0]] != word[index + 1]:
                    continue
                visited.add(child)
                ans = dfs(index + 1, child)
                visited.remove(child)
                if ans:
                    return True
            return False

        for start in starts:
            visited = set()
            result = dfs(0, start)
            if result:
                return result

        return False


if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    print(Solution().exist(board, word))