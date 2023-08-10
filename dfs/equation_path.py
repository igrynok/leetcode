from collections import defaultdict


class Solution(object):

    def dfs(self, graph, visited, query, node, path):

        if query[1] == node:
            return path

        for next_node in graph[node]:
            if next_node in visited:
                continue
            visited.add(next_node)
            ans = self.dfs(graph, visited, query, next_node[0], next_node[1]*path)
            if ans == -1:
                continue
            else:
                return ans

        return -1

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)
        for value, equation in zip(values, equations):

            graph[equation[0]].append((equation[1], value))
            graph[equation[1]].append((equation[0], 1/value))

        answer = []

        for index, query in enumerate(queries):
            visited = set()
            if query[0] not in graph or query[1] not in graph:
                answer.append(-1)
            else:
                answer.append(self.dfs(graph, visited, query, query[0], 1))

        return answer


if __name__ == '__main__':
    equations, values, queries = [["a","b"],["b","c"], ["b","d"]], [2.0,3.0,4.0], [["a","d"]]
    print(Solution().calcEquation(equations, values, queries))