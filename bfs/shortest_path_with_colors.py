from collections import deque


class Solution(object):

    def get_neighbours(self, node, color, reds, blues):
        return reds[node] if color == 'red' else blues[node]

    def bfs(self, start_color, answer, reds, blues):

        visited = set()
        queue = deque([0])
        color = start_color

        level = 0
        while queue:
            level += 1
            nodes_num = len(queue)
            for i in range(nodes_num):
                node = queue.popleft()
                for child in self.get_neighbours(node, color, reds, blues):
                    if (child, color) in visited:
                        continue
                    answer[child] = min(answer[child], level) if answer[child] != -1 else level
                    visited.add((child, color))
                    queue.append(child)
            color = 'red' if color == 'blue' else 'blue'

    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """

        reds = {i: [] for i in range(n)}
        blues = {i: [] for i in range(n)}

        for edge in redEdges:
            reds[edge[0]].append(edge[1])

        for edge in blueEdges:
            blues[edge[0]].append(edge[1])

        answer = [-1]*n
        if 0 in reds or 0 in blues:
            answer[0] = 0

        self.bfs('red', answer, reds, blues)
        self.bfs('blue', answer, reds, blues)

        return answer


if __name__ == '__main__':
    print(Solution().shortestAlternatingPaths(5, [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]], [[1,3],[0,0],[0,3],[4,2],[1,0]]))
