from collections import deque, defaultdict


class Solution(object):

    def bfs(self, start, visited, graph):
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                if child in visited:
                    continue
                visited.add(child)
                queue.append(child)

    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        sccs = []

        for node in range(n):
            if node in visited:
                continue
            old = len(visited)
            self.bfs(node, visited, graph)
            new = len(visited)
            sccs.append(new - old)

        count = 0
        sum_sccs = sum(sccs)
        for i in range(len(sccs)):
            count += sccs[i]*(sum_sccs - sccs[i])

        return count


if __name__ == '__main__':
    print(Solution().countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]]))