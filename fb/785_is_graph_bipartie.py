from collections import deque


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        set_A, set_B = set(), set()

        for i in range(len(graph)):

            if i in set_A or i in set_B:
                continue

            queue = deque()
            visited = set()
            if len(graph[i]):
                set_A.add(i)
                queue.append(i)
                visited.add(i)

            while queue:
                node = queue.popleft()
                for child in graph[node]:
                    if node in set_A:
                        if child in set_A:
                            return False
                        set_B.add(child)
                    else:
                        if child in set_B:
                            return False
                        set_A.add(child)
                    if child in visited:
                        continue
                    visited.add(child)
                    queue.append(child)

        return True
