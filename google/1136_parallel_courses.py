from collections import deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        in_degree = {}
        out_degree = {}

        for i in range(1, n + 1):
            in_degree[i] = []
            out_degree[i] = []

        for rel in relations:
            in_degree[rel[1]].append(rel[0])
            out_degree[rel[0]].append(rel[1])

        semesters = 0
        courses = n

        queue = deque()

        for course in in_degree:
            if len(in_degree[course]) == 0:
                queue.append(course)

        while queue:
            semester_courses_n = len(queue)
            semesters += 1
            courses -= semester_courses_n
            for _ in range(semester_courses_n):
                course = queue.popleft()
                for next_course in out_degree[course]:
                    in_degree[next_course].remove(course)
                del in_degree[course]

            for c in in_degree:
                if len(in_degree[c]) == 0:
                    queue.append(c)

        return semesters if courses == 0 else -1