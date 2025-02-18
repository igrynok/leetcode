class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        max_path = ""

        def dfs(path, a, b, c):

            nonlocal max_path

            if len(path) > len(max_path):
                max_path = path

            if a > 0 and (len(path) < 2 or path[-2:] != "aa"):
                dfs(path + "a", a - 1, b, c)
            if b > 0 and (len(path) < 2 or path[-2:] != "bb"):
                dfs(path + "b", a, b - 1, c)
            if c > 0 and (len(path) < 2 or path[-2:] != "cc"):
                dfs(path + "c", a, b, c - 1)

        dfs("", a, b, c)