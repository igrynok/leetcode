from collections import defaultdict
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        pairs = defaultdict(list)
        min_diff = 10e8

        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] <= min_diff:
                min_diff = arr[i+1] - arr[i]
                pairs[min_diff].append([arr[i], arr[i+1]])

        return pairs[min_diff]
