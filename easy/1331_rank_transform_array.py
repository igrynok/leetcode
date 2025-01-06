from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        if not arr:
            return []

        arr_sorted = sorted(arr)
        ranks = {arr_sorted[0]: 1}
        rank = 1
        arr_prev = arr_sorted[0]
        for elem in arr_sorted[1:]:
            if elem == arr_prev:
                ranks[elem] = rank
            else:
                ranks[elem] = rank + 1
                rank += 1
            arr_prev = elem

        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]

        return arr
