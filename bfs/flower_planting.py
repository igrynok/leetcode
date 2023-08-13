from collections import defaultdict, deque


class Solution(object):

    def get_uncolored(self, answer):
        for index, a in enumerate(answer):
            if a == -1:
                return index + 1
        return -1

    def bfs(self, start, graph, answer):

        queue = deque([(start, 1)])
        answer[start - 1] = 1

        while len(queue) > 0:
            node = queue.popleft()

            for child in graph[node[0]]:
                if answer[child - 1] != -1:
                    continue

                colors = [color for color in [1, 2, 3, 4] if color != node[1]]
                for neighbour in graph[child]:

                    if answer[neighbour - 1] != -1:
                        if answer[neighbour - 1] in colors:
                            colors.remove(answer[neighbour - 1])

                color = colors.pop()
                answer[child - 1] = color
                queue.append((child, color))

        return answer

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

        while self.get_uncolored(answer) != -1 :
            uncolored = self.get_uncolored(answer)
            self.bfs(uncolored, graph, answer)

        return answer

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

        while self.get_uncolored(answer) != -1 :
            uncolored = self.get_uncolored(answer)
            self.bfs(uncolored, graph, answer)

        return answer


if __name__ == '__main__':
    print(Solution().gardenNoAdj(3, [[1,2],[2,3],[3,1]]))