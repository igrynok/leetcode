from collections import defaultdict, deque


class Solution(object):

    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """

        graph = defaultdict(list)
        for path in paths:
            graph[path[0]].append(path[1])
            graph[path[1]].append(path[0])

        answer = [-1]*n

        for i in range(1, n + 1):
            colors = [1, 2, 3, 4]
            for neighbour in graph[i]:
                if answer[neighbour - 1] != -1 and answer[neighbour - 1] in colors:
                    colors.remove(answer[neighbour - 1])
            answer[i - 1] = colors.pop()

        return answer


if __name__ == '__main__':
    print(Solution().gardenNoAdj(3, [[1,2],[2,3],[3,1]]))