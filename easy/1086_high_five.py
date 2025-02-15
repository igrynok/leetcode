from collections import defaultdict
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        scores = defaultdict(list)
        for student_id, score in items:
            scores[student_id].append(score)

        result = []
        for student_id, score_list in scores.items():
            top_five = sorted(score_list, reverse=True)[:5]
            avg = sum(top_five) // 5
            result.append([student_id, avg])

        result.sort(key=lambda x: x[0])

        return result