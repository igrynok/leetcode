class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        answer = []

        def dfs(index, path):

            if index == len(s):
                answer.append(path[:])

            for i in range(index + 1, len(s) + 1):
                if s[index:i] != s[index:i][::-1]:
                    continue
                path.append(s[index:i])
                dfs(i, path)
                path.pop()

        dfs(0, [])
        return answer


if __name__ == '__main__':
    print(Solution().partition('aab'))