class Solution(object):

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.count = 0
        answer = []

        def dfs(mask, level, path):
            if level == n + 1:
                if sum(mask) == 0:
                    self.count += 1
                    answer.append(path[:])
                return
            for i in range(1, n + 1):
                if mask[i] == 0:
                    continue
                if i % level == 0 or level % i == 0:
                    mask[i] = 0
                    path.append(i)
                    dfs(mask, level + 1, path)
                    mask[i] = 1
                    path.pop()

        mask = [1] * (n + 1)
        mask[0] = 0
        dfs(mask, 1, [])
        return self.count


if __name__ == '__main__':
    print(Solution().countArrangement(3))
